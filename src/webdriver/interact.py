from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from . import utils, wait

class Interactions(object):

    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.wait = wait.Wait(driver, timeout)

    def click_on_svg_element(self, css):
        '''click on an svg element
        
        Arguments
            css (str): css value describing the svg location
        '''
        script = '''var ev = document.createEvent("SVGEvents");
                 ev.initEvent("click",true,true);
                 var target = $("{value}").get(0);
                 target.dispatchEvent(ev);'''.format(value = css)

        return self.driver.execute_script(script)

    def click_button_with_text(self, text):
        '''click on any button that matches the text
        
        Arguments
            text (str): string matching text value
        '''
        script = '''return $('button:contains("%s")').click()''' % text

        return self.driver.execute_script(script)

    def click_link_with_text(self, text):
        '''click on any link with provided link text
        
        Arguments
            text (str): string matching link text
        '''

        return self.driver.find_element_by_link_text(text).click()

    def type_in_active_input_element(self, text):
        '''send text + enter key to active input element

        Arguments
            text (str): text to input
        '''

        self.driver.switch_to.active_element.send_keys(text + Keys.RETURN)

    def double_click(self, element = None, locator = None, **kwargs):
        '''double click on provided element or locator matching that element

        Arguments
            element (object): selenium element to double click on
            locator (tuple): selenium locator tuple or kwargs describing the 
                             location
        '''

        if not element:
            locator = utils.translate_arguments(locator, **kwargs)

            element = self.driver.find_element(locator)

        actionChains = ActionChains(self.driver)
        actionChains.double_click(element).perform()

    def hover(self, element = None, 
              x_offset = 0, y_offset = 0, locator = None, **kwargs):
        '''hover over a particular element

        Arguments
            element (object): selenium element to double click on
            locator (tuple): selenium locator tuple or kwargs describing the 
                             location
            x_offset/y_offset (int): pixel offets from uppler left top corner.
        '''
        
        if not element:
            locator = utils.translate_arguments(locator, **kwargs)

            element = self.driver.find_element(locator)
        
        actionChains = ActionChains(self.driver)

        if x_offset or y_offset:
            actionChains.move_to_element_with_offset(element, 
                                                     x_offset, 
                                                     y_offset).perform()
        else:
            actionChains.move_to_element(element).perform()

    def select_from_drop_down(self, option, locator = None, **kwargs):
        '''select text from drop down list

        Arguments
            option (text): text to match for selection
            locator (tuple): selenium locator tuple or kwargs describing the 
                             location
        '''
        locator = utils.translate_arguments(locator, **kwargs)

        element = self.wait.until.visibility_of_element_located(locator)
        select = Select(element)
        select.select_by_visible_text(option)

    def type_and_enter(self, value, locator = None, **kwargs):
        '''send text + enter key to located element

        Arguments
            text (str): text to input
            locator (tuple): selenium locator tuple or kwargs describing the 
                             location
        '''
        locator = utils.translate_arguments(locator, **kwargs)

        element = self.wait.until.visibility_of_element_located(locator)
        return element.send_keys(value, Keys.RETURN)

    def send_return(self, locator = None, **kwargs):
        '''send enter key to located element

        Arguments
            locator (tuple): selenium locator tuple or kwargs describing the 
                             location
        '''

        locator = utils.translate_arguments(locator, **kwargs)

        element = self.wait.until.visibility_of_element_located(locator)

        return element.send_keys(Keys.RETURN)

    def send_tab(self, locator = None, **kwargs):
        '''send tab key to located element

        Arguments
            locator (tuple): selenium locator tuple or kwargs describing the 
                             location
        '''
        locator = utils.translate_arguments(locator, **kwargs)

        element = self.wait.until.visibility_of_element_located(locator)
        return element.send_keys(Keys.TAB)

    def drag_and_drop(self, source, dest):
        '''Drags and drops element from source to destination.

        Arguments
            source (tuple): locator that needs to be dragged
            dest (tuple): locator that needs to be dropped to
        '''

        source = self.wait.until.visibility_of_element_located(source)
        dest = self.wait.until.visibility_of_element_located(dest)
        self.drag_and_drop_element(source, dest)

    def drag_and_drop_element(self, source, dest):
        '''Drags and drops element from source to destination.

        Arguments
            source (element): name of the element that needs to be dragged
            dest (element): name of the element that needs to be dropped to
        '''

        ActionChains(self.driver).drag_and_drop(source, dest).perform()


    def scroll_into_view(self, element = None, locator = None, **kwargs):
        '''scroll provided element/location into view

        Arguments
            element (object): selenium element to double click on
            locator (tuple): selenium locator tuple or kwargs describing the 
                             location
        '''

        if not element:
            locator = utils.translate_arguments(locator, **kwargs)

            element = self.wait.until.visibility_of_element_located(locator)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", 
                                   element)

    def jquery_click(self, css):
        '''perform a jquery click on provided css element

        Arguments
            css (str): css value describing the svg location
        '''

        self.driver.execute_script("$('%s').click()" % css)
