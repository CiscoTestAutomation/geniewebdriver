from . import utils

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

__all__ = ['PageElement', 'TextBox', 'Button', 'RadioButton', 
           'Checkbox', 'Selector']

class PageElement(object):
    '''
    Descriptor class to allow enhancement to WebPage classes by adding 
    additional functionality without explicitly writing a lot of code
    '''
    
    def __init__(self, locator = None, **kwargs):
        self.locator = utils.translate_arguments(locator, **kwargs)

    def __set__(self, obj, value):
        raise NotImplementedError('PageElement only supports get methods until '
                                  'a proper set method is added through '
                                  'subclassing')

    def __get__(self, obj, owner):
        return obj.driver.find_element(*self.locator)


class TextBox(PageElement):

    def __init__(self, locator = None, value = None, **kwargs):
        if value:
            self.locator = (By.XPATH,
                            ".//input[@type='text' and @value='%s']" % value)
        else:
            self.locator = utils.translate_arguments(locator, **kwargs)


    def __set__(self, obj, value):
        element = obj.wait.until.visibility_of_element_located(self.locator)
        element.clear()
        element.send_keys(str(value))

    def __get__(self, obj, owner):
        element = obj.wait.until.visibility_of_element_located(self.locator)
        return element.get_attribute('value')

class Button(PageElement):

    def __get__(self, obj, owner):
        return obj.wait.until.element_to_be_clickable(self.locator)

class RadioButton(PageElement):

    def __init__(self, locator = None, value = None, **kwargs):

        if value:
            self.locator = (By.XPATH,
                            ".//input[@type='radio' and @value='%s']" % value)
        else:
            self.locator = utils.translate_arguments(locator, **kwargs)

    def __get__(self, obj, owner):
        element = obj.wait.until.element_to_be_clickable(self.locator)

        return element.is_selected()

    def __set__(self, obj, value):
        if value:
            element = obj.wait.until.element_to_be_clickable(self.locator)
            element.click()

class Checkbox(PageElement):
    def __init__(self, locator = None, value = None, **kwargs):
        if value:
            self.locator = (By.XPATH,
                           ".//input[@type='checkbox' and @value='%s']" % value)
        else:
            self.locator = utils.translate_arguments(locator, **kwargs)

    def __get__(self, obj, owner):
        element = obj.wait.until.element_to_be_clickable(self.locator)
        return element.is_selected()

    def __set__(self, obj, check):
        element = obj.wait.until.element_to_be_clickable(self.locator)

        checked = element.is_selected()
        if (checked and not check) or (not checked and check):
            # click to toggle
            element.click()

class Selector(PageElement):

    def __get__(self, obj, owner):
        element = obj.wait.until.element_to_be_clickable(self.locator)

        # return a selector instance
        return Select(element)

    def __set__(self, *args):
        raise TypeError('Use the returned to select object to set values')
