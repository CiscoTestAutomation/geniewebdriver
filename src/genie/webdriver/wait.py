from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import utils

class Wait(object):
    '''
    Wait object, intended to be used as an attribute under page, for shortcut
    use of selenium wait/ec apis without explicitly having to import them and/or
    refer to their syntax.

    Example:
        # typical selenium code
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

        # using this wait class
        page = WebPage(driver)
        page.wait.until.element_to_be_clickable(id = 'someid', timeout = 10)
    '''

    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.until = WaitUntil(driver, timeout)
        self.until_not = WaitUntilNot(driver, timeout)

    def __call__(self, timeout = None):
        '''allows the Wait() instance to be called as if it was just an inline
        wait (implicitly_wait)

        Exmaple:
            page = WebPage(driver)
            page.wait(10)
        '''

        timeout = timeout or self.timeout

        return self.driver.implicitly_wait(timeout)


class WaitUntil(object):
    '''Class to allow users to perform a wait-until'''


    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def __call__(self, condition, timeout = None, message = '', **kwargs):
        '''same as WebDriverWait().until(), in a different argument form.'''
        
        return WebDriverWait(driver = self.driver, 
                             timeout = timeout or self.timeout, 
                             **kwargs).until(condition, message)


    def title_is(self, title, **kwargs): 
        """An expectation for checking the title of a page.
        title is the expected title, which must be an exact match
        returns True if the title matches, false otherwise.

        Arguments
            title (str): title to check for
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        condition = EC.title_is(title)
        
        return self(condition, **kwargs)


    def title_contains(self, title, **kwargs): 
        """An expectation for checking that the title contains a case-sensitive
        substring. title is the fragment of title expected
        returns True when the title matches, False otherwise

        Arguments
            title (str): title to check for
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        condition = EC.title_contains(title)
        
        return self(condition, **kwargs)


    def presence_of_element_located(self, locator = None, **kwargs):
        """ An expectation for checking that an element is present on the DOM
        of a page. This does not necessarily mean that the element is visible.
        locator - used to find the element
        returns the WebElement once it is located

        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.presence_of_element_located((By.ID, 'loginForm'), ...)

        is the same as
            WaitUntil.presence_of_element_located(id = 'loginForm', ...)

        Arguments
            locator (tuple): location describing the location by
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """

        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)
        condition = EC.presence_of_element_located(locator)

        return self(condition, **kwargs)


    def visibility_of_element_located(self, locator = None, **kwargs):
        """An expectation for checking that an element is present on the DOM of
        a page and visible. Visibility means that the element is not only 
        displayed but also has a height and width that is greater than 0.
        locator - used to find the element
        returns the WebElement once it is located and visible

        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.visibility_of_element_located((By.ID, 'loginForm'), ...)

        is the same as
            WaitUntil.visibility_of_element_located(id = 'loginForm', ...)

        Arguments
            locator (tuple): location describing the location by
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """

        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)
        condition = EC.visibility_of_element_located(locator)

        return self(condition, **kwargs)


    def visibility_of(self, element, **kwargs):
        """ An expectation for checking that an element, known to be present on 
        the DOM of a page, is visible. Visibility means that the element is not 
        only displayed but also has a height and width that is greater than 0.
        element is the WebElement
        returns the (same) WebElement once it is visible

        Arguments
            element (obj): element to check for
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        condition = EC.visibility_of(element)

        return self(condition, **kwargs)


    def presence_of_all_elements_located(self, locator = None, **kwargs):
        """ An expectation for checking that there is at least one element
        present on a web page.
        locator is used to find the element
        returns the list of WebElements once they are located

        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.presence_of_all_elements_located((By.ID, 'loginForm'), ..)

        is the same as
            WaitUntil.presence_of_all_elements_located(id = 'loginForm', ...)

        Arguments
            locator (tuple): location describing the location by
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api

        """
        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)
        condition = EC.presence_of_all_elements_located(locator)

        return self(condition, **kwargs)


    def visibility_of_any_elements_located(self, locator = None, **kwargs):
        """ An expectation for checking that there is at least one element 
        visible on a web page.
        locator is used to find the element
        returns the list of WebElements once they are located

        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.visibility_of_any_elements_located((By.ID, 'loginForm'),
                                                         ..)

        is the same as
            WaitUntil.visibility_of_any_elements_located(id = 'loginForm', ...)

        Arguments
            locator (tuple): location describing the location by
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api

        """
        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)
        condition = EC.visibility_of_any_elements_located(locator)

        return self(condition, **kwargs)


    def text_to_be_present_in_element(self, 
                                      *,
                                      text, 
                                      locator = None, 
                                      **kwargs):
        """ An expectation for checking if the given text is present in the
        specified element.
        locator, text

        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.text_to_be_present_in_element((By.ID, 'loginForm'), ..)

        is the same as
            WaitUntil.text_to_be_present_in_element(id = 'loginForm', ...)

        Arguments
            locator (tuple): location describing the location by
            text (str): text to search for in element
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)
        condition = EC.text_to_be_present_in_element(locator, text)

        return self(condition, **kwargs)


    def text_to_be_present_in_element_value(self, *,
                                            text, 
                                            locator = None, 
                                            **kwargs):
        """
        An expectation for checking if the given text is present in the 
        element's locator, text

        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.text_to_be_present_in_element_value((By.ID, 
                                                           'loginForm'), ..)

        is the same as
            WaitUntil.text_to_be_present_in_element_value(id = 'loginForm', ...)

        Arguments
            locator (tuple): location describing the location by
            text (str): text to search for in element
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)
        condition = EC.text_to_be_present_in_element_value(locator, text)

        return self(condition, **kwargs)


    def frame_to_be_available_and_switch_to_it(self, locator = None, **kwargs):
        """ An expectation for checking whether the given frame is available to
        switch to.  If the frame is available it switches the given driver to
        the specified frame.

        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.frame_to_be_available_and_switch_to_it((By.ID, 
                                                           'loginForm'), ..)

        is the same as
            WaitUntil.frame_to_be_available_and_switch_to_it(id = 'loginForm', 
                                                             ...)

        Arguments
            locator (tuple): location describing the location by
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)
        condition = EC.frame_to_be_available_and_switch_to_it(locator)

        return self(condition, **kwargs)


    def invisibility_of_element_located(self, locator = None, **kwargs):
        """ An Expectation for checking that an element is either invisible 
        or not present on the DOM.

        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.invisibility_of_element_located((By.ID, 
                                                           'loginForm'), ..)

        is the same as
            WaitUntil.invisibility_of_element_located(id = 'loginForm', 
                                                             ...)

        Arguments
            locator (tuple): location describing the location by
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)
        condition = EC.invisibility_of_element_located(locator)

        return self(condition, **kwargs)


    def element_to_be_clickable(self, locator = None, **kwargs):
        """ An Expectation for checking an element is visible and enabled such 
        that you can click it

        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.element_to_be_clickable((By.ID, 'loginForm'), ..)

        is the same as
            WaitUntil.element_to_be_clickable(id = 'loginForm', ...)

        Arguments
            locator (tuple): location describing the location by
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)
        condition = EC.element_to_be_clickable(locator)

        return self(condition,**kwargs)


    def staleness_of(self, element, **kwargs):
        """ Wait until an element is no longer attached to the DOM.
        element is the element to wait for.
        returns False if the element is still attached to the DOM, true 
        otherwise.

        Arguments
            element (obj): element to check for
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        condition = EC.staleness_of(element)

        return self(condition, **kwargs)


    def element_to_be_selected(self, element, **kwargs):
        """ An expectation for checking the selection is selected.
        element is WebElement object

        Arguments
            element (obj): element to check for
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        condition = EC.element_to_be_selected(element)

        return self(condition, **kwargs)


    def element_located_to_be_selected(self, locator = None, **kwargs):
        """An expectation for the element to be located is selected.
        locator is a tuple of (by, path)
        
        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.element_located_to_be_selected((By.ID, 'loginForm'), ..)

        is the same as
            WaitUntil.element_located_to_be_selected(id = 'loginForm', ...)

        Arguments
            locator (tuple): location describing the location by
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)
        condition = EC.element_located_to_be_selected(locator)

        return self(condition, **kwargs)


    def element_selection_state_to_be(self, element, state, **kwargs):
        """ An expectation for checking if the given element is selected.
        element is WebElement object

        Arguments
            element (obj): element to check for
            state (bool): true or false
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        condition = EC.element_selection_state_to_be(element, state)

        return self(condition, **kwargs)


    def element_located_selection_state_to_be(self, *,
                                              state, 
                                              locator = None, 
                                              **kwargs):
        """An expectation to locate an element and check if the selection state
        specified is in that state.
        
        This API supports kwargs style location-by shorthand. Eg:
            WaitUntil.element_located_selection_state_to_be((By.ID, 
                                                            'loginForm'), ..)

        is the same as
            WaitUntil.element_located_selection_state_to_be(id = 'loginForm', 
                                                            ...)

        Arguments
            locator (tuple): location describing the location by
            state (bool): true or false
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """

        locator, kwargs = utils.translate_args_with_passthru(locator, **kwargs)

        condition = EC.element_located_selection_state_to_be(locator, state)

        return self(condition, **kwargs)


    def number_of_windows_to_be(self, num_windows, **kwargs):
        """ An expectation for the number of windows to be a certain value.
    
        Arguments
            num_windows (int): number of windows
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        condition = EC.number_of_windows_to_be(num_windows)

        return self(condition, **kwargs)

    def new_window_is_opened(self, current_handles, **kwargs):
        """ An expectation that a new window will be opened and have the number
        of windows handles increase
        
        Arguments
            current_handles (obj): current handle object
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        condition = EC.new_window_is_opened(current_handles)

        return self(condition, **kwargs)


    def alert_is_present(self, **kwargs):
        """ Expect an alert to be present.

        Arguments
            timeout (int): seconds to wait for
            message (str): message to display if timed out
            kwargs (dict): any other argument for WebDriverWait() api
        """
        condition = EC.alert_is_present()

        return self(condition, **kwargs)


class WaitUntilNot(WaitUntil):
    '''Class to allow users to perform a wait-until-not'''

    def __call__(self, condition, timeout = None, message = '', **kwargs):

        return WebDriverWait(driver = self.driver, 
                             timeout = timeout or self.timeout, 
                             **kwargs).until_not(condition, message)