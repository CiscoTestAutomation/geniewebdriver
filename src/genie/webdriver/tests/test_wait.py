import unittest
from unittest.mock import patch, Mock

class Test_Wait(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global Wait

        from genie.webdriver.wait import Wait

    def setUp(self):
        self.driver = Mock()

    def test_init(self):
        with patch('genie.webdriver.wait.WaitUntil') as wu:
            with patch('genie.webdriver.wait.WaitUntilNot') as wun:
                wait = Wait(driver = self.driver, timeout = 10)
                self.assertEqual(wait.timeout, 10)
                self.assertIs(wait.driver, self.driver)

                wu.assert_called_with(self.driver, 10)
                wun.assert_called_with(self.driver, 10)

        wait = Wait(driver = self.driver, timeout = 10)

        from genie.webdriver.wait import WaitUntil, WaitUntilNot
        self.assertTrue(isinstance(wait.until, WaitUntil))
        self.assertTrue(isinstance(wait.until_not, WaitUntilNot))

    def test_call(self):
        wait = Wait(driver = self.driver, timeout = 10)
        wait(10)

        self.driver.implicitly_wait.assert_called_with(10)

    def test_until(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            wait = Wait(driver = self.driver, timeout = 10)
            wait.until(object, message='lalala')

            wdw.assert_called_with(driver = self.driver, timeout = 10)
            wdw().until.assert_called_with(object, 'lalala')

        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            wait = Wait(driver = self.driver, timeout = 10)
            wait.until(object, message='lalala', abc=1)

            wdw.assert_called_with(driver = self.driver, timeout = 10, abc=1)
            wdw().until.assert_called_with(object, 'lalala')

    def test_until_not(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            wait = Wait(driver = self.driver, timeout = 10)
            wait.until_not(object, message='lalala')

            wdw.assert_called_with(driver = self.driver, timeout = 10)
            wdw().until_not.assert_called_with(object, 'lalala')

        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            wait = Wait(driver = self.driver, timeout = 10)
            wait.until_not(object, message='lalala', abc=1)

            wdw.assert_called_with(driver = self.driver, timeout = 10, abc=1)
            wdw().until_not.assert_called_with(object, 'lalala')

class Test_WaitUntil(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global WaitUntil, By

        from genie.webdriver.wait import WaitUntil
        from selenium.webdriver.common.by import By

    def setUp(self):
        self.driver = Mock()

    def test_init(self):
        wait = WaitUntil(driver = self.driver, timeout = 10)
        self.assertEqual(wait.timeout, 10)
        self.assertIs(wait.driver, self.driver)

    def test_call(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            wait = WaitUntil(driver = self.driver, timeout = 10)
            wait(object, message='lalala')

            wdw.assert_called_with(driver = self.driver, timeout = 10)
            wdw().until.assert_called_with(object, 'lalala')

    def test_title_is(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.title_is('jb is genius')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.title_is.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_is(), '')

        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 61)
                wait.title_is('jb is genius', message = 'boom')

                wdw.assert_called_with(driver = self.driver, timeout = 61)
                ec.title_is.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_is(), 'boom')

    def test_title_contains(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.title_contains('jb is genius')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.title_contains.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_contains(), '')

        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 61)
                wait.title_contains('jb is genius', message = 'boom')

                wdw.assert_called_with(driver = self.driver, timeout = 61)
                ec.title_contains.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_contains(), 'boom')

    def test_presence_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.presence_of_element_located(css='lalala', message = 'monk',
                                                 timeout = 11)

                wdw.assert_called_with(driver = self.driver, timeout = 11)
                ec.presence_of_element_located.assert_called_with(
                                    (By.CSS_SELECTOR, 'lalala'))
                wdw().until.assert_called_with(ec.presence_of_element_located(), 
                                               'monk')

    def test_visibility_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.visibility_of_element_located(
                                    name='lalala1', message = 'monk',
                                                 timeout = 13)

                wdw.assert_called_with(driver = self.driver, timeout = 13)
                ec.visibility_of_element_located.assert_called_with(
                                    (By.NAME, 'lalala1'))
                wdw().until.assert_called_with(
                            ec.visibility_of_element_located(), 
                                               'monk')

    def test_visibility_of(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.visibility_of(object, message = 'monk',
                                                 timeout = 14)

                wdw.assert_called_with(driver = self.driver, timeout = 14)
                ec.visibility_of.assert_called_with(object)
                wdw().until.assert_called_with(ec.visibility_of(), 'monk')

    def test_presence_of_all_elements_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.presence_of_all_elements_located(
                                    link='legion', message = 'willnotprevail',
                                                 timeout = 15)

                wdw.assert_called_with(driver = self.driver, timeout = 15)
                ec.presence_of_all_elements_located.assert_called_with(
                                    (By.LINK_TEXT, 'legion'))
                wdw().until.assert_called_with(
                            ec.presence_of_all_elements_located(), 
                                               'willnotprevail')

    def test_text_to_be_present_in_element(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element(text = '111',
                                    tag='paladin', timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element(), 
                                               '')
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element(text = '111',
                                    locator = (By.TAG_NAME, 'paladin'), 
                                    timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element(), 
                                               '')

    def test_text_to_be_present_in_element_value(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element_value(text = '111',
                                    tag='paladin', timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element_value.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element_value(), 
                                               '')
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element_value(text = '111',
                                    locator = (By.TAG_NAME, 'paladin'), 
                                    timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element_value.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element_value(), 
                                               '')

    def test_frame_to_be_available_and_switch_to_it(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.frame_to_be_available_and_switch_to_it(
                                    tag_name='warrior', timeout = 17)

                wdw.assert_called_with(driver = self.driver, timeout = 17)
                ec.frame_to_be_available_and_switch_to_it.assert_called_with(
                                    (By.TAG_NAME, 'warrior'))
                wdw().until.assert_called_with(
                            ec.frame_to_be_available_and_switch_to_it(), 
                                               '')
    
    def test_invisibility_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.invisibility_of_element_located(
                                    (By.ID, 'priest'), timeout = 17)

                wdw.assert_called_with(driver = self.driver, timeout = 17)
                ec.invisibility_of_element_located.assert_called_with(
                                    (By.ID, 'priest'))
                wdw().until.assert_called_with(
                            ec.invisibility_of_element_located(), 
                                               '')
    
    def test_element_to_be_clickable(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_to_be_clickable(
                                    (By.ID, 'lol'), timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.element_to_be_clickable.assert_called_with(
                                    (By.ID, 'lol'))
                wdw().until.assert_called_with(
                            ec.element_to_be_clickable(), 
                                               '')

    def test_staleness_of(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.staleness_of(self, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.staleness_of.assert_called_with(self)
                wdw().until.assert_called_with(
                            ec.staleness_of(), 
                                               '')

    def test_element_to_be_selected(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_to_be_selected(self, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.element_to_be_selected.assert_called_with(self)
                wdw().until.assert_called_with(
                            ec.element_to_be_selected(), 
                                               '')

    def test_element_located_to_be_selected(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_located_to_be_selected(class_ = 'ddy', 
                                                    timeout = 21)

                wdw.assert_called_with(driver = self.driver, timeout = 21)
                ec.element_located_to_be_selected.assert_called_with(
                                    (By.CLASS_NAME, 'ddy'))
                wdw().until.assert_called_with(
                            ec.element_located_to_be_selected(), 
                                               '')

    def test_element_selection_state_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_selection_state_to_be(self, 'up!')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.element_selection_state_to_be.assert_called_with(
                                    self, 'up!')
                wdw().until.assert_called_with(
                            ec.element_selection_state_to_be(), 
                                               '')

    def test_element_located_selection_state_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_located_selection_state_to_be(
                                                    class_name = 'jalopnik',
                                                    state = 'down!',
                                                    timeout = 23)

                wdw.assert_called_with(driver = self.driver, timeout = 23)
                ec.element_located_selection_state_to_be.assert_called_with(
                                    (By.CLASS_NAME, 'jalopnik'), 'down!')
                wdw().until.assert_called_with(
                            ec.element_located_selection_state_to_be(), 
                                               '')

    def test_number_of_windows_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.number_of_windows_to_be(111, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.number_of_windows_to_be.assert_called_with(111)
                wdw().until.assert_called_with(
                            ec.number_of_windows_to_be(), 
                                               '')

    def test_new_window_is_opened(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.new_window_is_opened(111, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.new_window_is_opened.assert_called_with(111)
                wdw().until.assert_called_with(
                            ec.new_window_is_opened(), 
                                               '')

    def test_alert_is_present(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.alert_is_present(timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.alert_is_present.assert_called_with()
                wdw().until.assert_called_with(
                            ec.alert_is_present(), 
                                               '')

class Test_WaitUntil(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global WaitUntil, By

        from genie.webdriver.wait import WaitUntil
        from selenium.webdriver.common.by import By

    def setUp(self):
        self.driver = Mock()

    def test_init(self):
        wait = WaitUntil(driver = self.driver, timeout = 10)
        self.assertEqual(wait.timeout, 10)
        self.assertIs(wait.driver, self.driver)

    def test_call(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            wait = WaitUntil(driver = self.driver, timeout = 10)
            wait(object, message='lalala')

            wdw.assert_called_with(driver = self.driver, timeout = 10)
            wdw().until.assert_called_with(object, 'lalala')

    def test_title_is(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.title_is('jb is genius')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.title_is.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_is(), '')

        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 61)
                wait.title_is('jb is genius', message = 'boom')

                wdw.assert_called_with(driver = self.driver, timeout = 61)
                ec.title_is.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_is(), 'boom')

    def test_title_contains(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.title_contains('jb is genius')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.title_contains.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_contains(), '')

        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 61)
                wait.title_contains('jb is genius', message = 'boom')

                wdw.assert_called_with(driver = self.driver, timeout = 61)
                ec.title_contains.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_contains(), 'boom')

    def test_presence_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.presence_of_element_located(css='lalala', message = 'monk',
                                                 timeout = 11)

                wdw.assert_called_with(driver = self.driver, timeout = 11)
                ec.presence_of_element_located.assert_called_with(
                                    (By.CSS_SELECTOR, 'lalala'))
                wdw().until.assert_called_with(ec.presence_of_element_located(), 
                                               'monk')

    def test_visibility_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.visibility_of_element_located(
                                    name='lalala1', message = 'monk',
                                                 timeout = 13)

                wdw.assert_called_with(driver = self.driver, timeout = 13)
                ec.visibility_of_element_located.assert_called_with(
                                    (By.NAME, 'lalala1'))
                wdw().until.assert_called_with(
                            ec.visibility_of_element_located(), 
                                               'monk')

    def test_visibility_of(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.visibility_of(object, message = 'monk',
                                                 timeout = 14)

                wdw.assert_called_with(driver = self.driver, timeout = 14)
                ec.visibility_of.assert_called_with(object)
                wdw().until.assert_called_with(ec.visibility_of(), 'monk')

    def test_presence_of_all_elements_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.presence_of_all_elements_located(
                                    link='legion', message = 'willnotprevail',
                                                 timeout = 15)

                wdw.assert_called_with(driver = self.driver, timeout = 15)
                ec.presence_of_all_elements_located.assert_called_with(
                                    (By.LINK_TEXT, 'legion'))
                wdw().until.assert_called_with(
                            ec.presence_of_all_elements_located(), 
                                               'willnotprevail')

    def test_text_to_be_present_in_element(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element(text = '111',
                                    tag='paladin', timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element(), 
                                               '')
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element(text = '111',
                                    locator = (By.TAG_NAME, 'paladin'), 
                                    timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element(), 
                                               '')

    def test_text_to_be_present_in_element_value(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element_value(text = '111',
                                    tag='paladin', timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element_value.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element_value(), 
                                               '')
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element_value(text = '111',
                                    locator = (By.TAG_NAME, 'paladin'), 
                                    timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element_value.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element_value(), 
                                               '')

    def test_frame_to_be_available_and_switch_to_it(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.frame_to_be_available_and_switch_to_it(
                                    tag_name='warrior', timeout = 17)

                wdw.assert_called_with(driver = self.driver, timeout = 17)
                ec.frame_to_be_available_and_switch_to_it.assert_called_with(
                                    (By.TAG_NAME, 'warrior'))
                wdw().until.assert_called_with(
                            ec.frame_to_be_available_and_switch_to_it(), 
                                               '')
    
    def test_invisibility_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.invisibility_of_element_located(
                                    (By.ID, 'priest'), timeout = 17)

                wdw.assert_called_with(driver = self.driver, timeout = 17)
                ec.invisibility_of_element_located.assert_called_with(
                                    (By.ID, 'priest'))
                wdw().until.assert_called_with(
                            ec.invisibility_of_element_located(), 
                                               '')
    
    def test_element_to_be_clickable(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_to_be_clickable(
                                    (By.ID, 'lol'), timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.element_to_be_clickable.assert_called_with(
                                    (By.ID, 'lol'))
                wdw().until.assert_called_with(
                            ec.element_to_be_clickable(), 
                                               '')

    def test_staleness_of(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.staleness_of(self, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.staleness_of.assert_called_with(self)
                wdw().until.assert_called_with(
                            ec.staleness_of(), 
                                               '')

    def test_element_to_be_selected(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_to_be_selected(self, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.element_to_be_selected.assert_called_with(self)
                wdw().until.assert_called_with(
                            ec.element_to_be_selected(), 
                                               '')

    def test_element_located_to_be_selected(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_located_to_be_selected(class_ = 'ddy', 
                                                    timeout = 21)

                wdw.assert_called_with(driver = self.driver, timeout = 21)
                ec.element_located_to_be_selected.assert_called_with(
                                    (By.CLASS_NAME, 'ddy'))
                wdw().until.assert_called_with(
                            ec.element_located_to_be_selected(), 
                                               '')

    def test_element_selection_state_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_selection_state_to_be(self, 'up!')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.element_selection_state_to_be.assert_called_with(
                                    self, 'up!')
                wdw().until.assert_called_with(
                            ec.element_selection_state_to_be(), 
                                               '')

    def test_element_located_selection_state_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_located_selection_state_to_be(
                                                    class_name = 'jalopnik',
                                                    state = 'down!',
                                                    timeout = 23)

                wdw.assert_called_with(driver = self.driver, timeout = 23)
                ec.element_located_selection_state_to_be.assert_called_with(
                                    (By.CLASS_NAME, 'jalopnik'), 'down!')
                wdw().until.assert_called_with(
                            ec.element_located_selection_state_to_be(), 
                                               '')

    def test_number_of_windows_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.number_of_windows_to_be(111, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.number_of_windows_to_be.assert_called_with(111)
                wdw().until.assert_called_with(
                            ec.number_of_windows_to_be(), 
                                               '')

    def test_new_window_is_opened(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.new_window_is_opened(111, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.new_window_is_opened.assert_called_with(111)
                wdw().until.assert_called_with(
                            ec.new_window_is_opened(), 
                                               '')

    def test_alert_is_present(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.alert_is_present(timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.alert_is_present.assert_called_with()
                wdw().until.assert_called_with(
                            ec.alert_is_present(), 
                                               '')

class Test_WaitUntil(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global WaitUntil, By

        from genie.webdriver.wait import WaitUntil
        from selenium.webdriver.common.by import By

    def setUp(self):
        self.driver = Mock()

    def test_init(self):
        wait = WaitUntil(driver = self.driver, timeout = 10)
        self.assertEqual(wait.timeout, 10)
        self.assertIs(wait.driver, self.driver)

    def test_call(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            wait = WaitUntil(driver = self.driver, timeout = 10)
            wait(object, message='lalala')

            wdw.assert_called_with(driver = self.driver, timeout = 10)
            wdw().until.assert_called_with(object, 'lalala')

    def test_title_is(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.title_is('jb is genius')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.title_is.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_is(), '')

        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 61)
                wait.title_is('jb is genius', message = 'boom')

                wdw.assert_called_with(driver = self.driver, timeout = 61)
                ec.title_is.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_is(), 'boom')

    def test_title_contains(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.title_contains('jb is genius')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.title_contains.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_contains(), '')

        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 61)
                wait.title_contains('jb is genius', message = 'boom')

                wdw.assert_called_with(driver = self.driver, timeout = 61)
                ec.title_contains.assert_called_with('jb is genius')
                wdw().until.assert_called_with(ec.title_contains(), 'boom')

    def test_presence_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.presence_of_element_located(css='lalala', message = 'monk',
                                                 timeout = 11)

                wdw.assert_called_with(driver = self.driver, timeout = 11)
                ec.presence_of_element_located.assert_called_with(
                                    (By.CSS_SELECTOR, 'lalala'))
                wdw().until.assert_called_with(ec.presence_of_element_located(), 
                                               'monk')

    def test_visibility_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.visibility_of_element_located(
                                    name='lalala1', message = 'monk',
                                                 timeout = 13)

                wdw.assert_called_with(driver = self.driver, timeout = 13)
                ec.visibility_of_element_located.assert_called_with(
                                    (By.NAME, 'lalala1'))
                wdw().until.assert_called_with(
                            ec.visibility_of_element_located(), 
                                               'monk')

    def test_visibility_of(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.visibility_of(object, message = 'monk',
                                                 timeout = 14)

                wdw.assert_called_with(driver = self.driver, timeout = 14)
                ec.visibility_of.assert_called_with(object)
                wdw().until.assert_called_with(ec.visibility_of(), 'monk')

    def test_presence_of_all_elements_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.presence_of_all_elements_located(
                                    link='legion', message = 'willnotprevail',
                                                 timeout = 15)

                wdw.assert_called_with(driver = self.driver, timeout = 15)
                ec.presence_of_all_elements_located.assert_called_with(
                                    (By.LINK_TEXT, 'legion'))
                wdw().until.assert_called_with(
                            ec.presence_of_all_elements_located(), 
                                               'willnotprevail')

    def test_text_to_be_present_in_element(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element(text = '111',
                                    tag='paladin', timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element(), 
                                               '')
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element(text = '111',
                                    locator = (By.TAG_NAME, 'paladin'), 
                                    timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element(), 
                                               '')

    def test_text_to_be_present_in_element_value(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element_value(text = '111',
                                    tag='paladin', timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element_value.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element_value(), 
                                               '')
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element_value(text = '111',
                                    locator = (By.TAG_NAME, 'paladin'), 
                                    timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element_value.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until.assert_called_with(
                            ec.text_to_be_present_in_element_value(), 
                                               '')

    def test_frame_to_be_available_and_switch_to_it(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.frame_to_be_available_and_switch_to_it(
                                    tag_name='warrior', timeout = 17)

                wdw.assert_called_with(driver = self.driver, timeout = 17)
                ec.frame_to_be_available_and_switch_to_it.assert_called_with(
                                    (By.TAG_NAME, 'warrior'))
                wdw().until.assert_called_with(
                            ec.frame_to_be_available_and_switch_to_it(), 
                                               '')
    
    def test_invisibility_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.invisibility_of_element_located(
                                    (By.ID, 'priest'), timeout = 17)

                wdw.assert_called_with(driver = self.driver, timeout = 17)
                ec.invisibility_of_element_located.assert_called_with(
                                    (By.ID, 'priest'))
                wdw().until.assert_called_with(
                            ec.invisibility_of_element_located(), 
                                               '')
    
    def test_element_to_be_clickable(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_to_be_clickable(
                                    (By.ID, 'lol'), timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.element_to_be_clickable.assert_called_with(
                                    (By.ID, 'lol'))
                wdw().until.assert_called_with(
                            ec.element_to_be_clickable(), 
                                               '')

    def test_staleness_of(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.staleness_of(self, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.staleness_of.assert_called_with(self)
                wdw().until.assert_called_with(
                            ec.staleness_of(), 
                                               '')

    def test_element_to_be_selected(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_to_be_selected(self, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.element_to_be_selected.assert_called_with(self)
                wdw().until.assert_called_with(
                            ec.element_to_be_selected(), 
                                               '')

    def test_element_located_to_be_selected(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_located_to_be_selected(class_ = 'ddy', 
                                                    timeout = 21)

                wdw.assert_called_with(driver = self.driver, timeout = 21)
                ec.element_located_to_be_selected.assert_called_with(
                                    (By.CLASS_NAME, 'ddy'))
                wdw().until.assert_called_with(
                            ec.element_located_to_be_selected(), 
                                               '')

    def test_element_selection_state_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_selection_state_to_be(self, 'up!')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.element_selection_state_to_be.assert_called_with(
                                    self, 'up!')
                wdw().until.assert_called_with(
                            ec.element_selection_state_to_be(), 
                                               '')

    def test_element_located_selection_state_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.element_located_selection_state_to_be(
                                                    class_name = 'jalopnik',
                                                    state = 'down!',
                                                    timeout = 23)

                wdw.assert_called_with(driver = self.driver, timeout = 23)
                ec.element_located_selection_state_to_be.assert_called_with(
                                    (By.CLASS_NAME, 'jalopnik'), 'down!')
                wdw().until.assert_called_with(
                            ec.element_located_selection_state_to_be(), 
                                               '')

    def test_number_of_windows_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.number_of_windows_to_be(111, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.number_of_windows_to_be.assert_called_with(111)
                wdw().until.assert_called_with(
                            ec.number_of_windows_to_be(), 
                                               '')

    def test_new_window_is_opened(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.new_window_is_opened(111, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.new_window_is_opened.assert_called_with(111)
                wdw().until.assert_called_with(
                            ec.new_window_is_opened(), 
                                               '')

    def test_alert_is_present(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntil(driver = self.driver, timeout = 10)
                wait.alert_is_present(timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.alert_is_present.assert_called_with()
                wdw().until.assert_called_with(
                            ec.alert_is_present(), 
                                               '')

class Test_WaitUntilNot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global WaitUntilNot, By

        from genie.webdriver.wait import WaitUntilNot
        from selenium.webdriver.common.by import By

    def setUp(self):
        self.driver = Mock()

    def test_init(self):
        wait = WaitUntilNot(driver = self.driver, timeout = 10)
        self.assertEqual(wait.timeout, 10)
        self.assertIs(wait.driver, self.driver)

    def test_call(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            wait = WaitUntilNot(driver = self.driver, timeout = 10)
            wait(object, message='lalala')

            wdw.assert_called_with(driver = self.driver, timeout = 10)
            wdw().until_not.assert_called_with(object, 'lalala')

    def test_title_is(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.title_is('jb is genius')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.title_is.assert_called_with('jb is genius')
                wdw().until_not.assert_called_with(ec.title_is(), '')

        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 61)
                wait.title_is('jb is genius', message = 'boom')

                wdw.assert_called_with(driver = self.driver, timeout = 61)
                ec.title_is.assert_called_with('jb is genius')
                wdw().until_not.assert_called_with(ec.title_is(), 'boom')

    def test_title_contains(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.title_contains('jb is genius')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.title_contains.assert_called_with('jb is genius')
                wdw().until_not.assert_called_with(ec.title_contains(), '')

        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 61)
                wait.title_contains('jb is genius', message = 'boom')

                wdw.assert_called_with(driver = self.driver, timeout = 61)
                ec.title_contains.assert_called_with('jb is genius')
                wdw().until_not.assert_called_with(ec.title_contains(), 'boom')

    def test_presence_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.presence_of_element_located(css='lalala', message = 'monk',
                                                 timeout = 11)

                wdw.assert_called_with(driver = self.driver, timeout = 11)
                ec.presence_of_element_located.assert_called_with(
                                    (By.CSS_SELECTOR, 'lalala'))
                wdw().until_not.assert_called_with(ec.presence_of_element_located(), 
                                               'monk')

    def test_visibility_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.visibility_of_element_located(
                                    name='lalala1', message = 'monk',
                                                 timeout = 13)

                wdw.assert_called_with(driver = self.driver, timeout = 13)
                ec.visibility_of_element_located.assert_called_with(
                                    (By.NAME, 'lalala1'))
                wdw().until_not.assert_called_with(
                            ec.visibility_of_element_located(), 
                                               'monk')

    def test_visibility_of(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.visibility_of(object, message = 'monk',
                                                 timeout = 14)

                wdw.assert_called_with(driver = self.driver, timeout = 14)
                ec.visibility_of.assert_called_with(object)
                wdw().until_not.assert_called_with(ec.visibility_of(), 'monk')

    def test_presence_of_all_elements_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.presence_of_all_elements_located(
                                    link='legion', message = 'willnotprevail',
                                                 timeout = 15)

                wdw.assert_called_with(driver = self.driver, timeout = 15)
                ec.presence_of_all_elements_located.assert_called_with(
                                    (By.LINK_TEXT, 'legion'))
                wdw().until_not.assert_called_with(
                            ec.presence_of_all_elements_located(), 
                                               'willnotprevail')

    def test_text_to_be_present_in_element(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element(text = '111',
                                    tag='paladin', timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until_not.assert_called_with(
                            ec.text_to_be_present_in_element(), 
                                               '')
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element(text = '111',
                                    locator = (By.TAG_NAME, 'paladin'), 
                                    timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until_not.assert_called_with(
                            ec.text_to_be_present_in_element(), 
                                               '')

    def test_text_to_be_present_in_element_value(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element_value(text = '111',
                                    tag='paladin', timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element_value.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until_not.assert_called_with(
                            ec.text_to_be_present_in_element_value(), 
                                               '')
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.text_to_be_present_in_element_value(text = '111',
                                    locator = (By.TAG_NAME, 'paladin'), 
                                    timeout = 16)

                wdw.assert_called_with(driver = self.driver, timeout = 16)
                ec.text_to_be_present_in_element_value.assert_called_with(
                                    (By.TAG_NAME, 'paladin'), '111')
                wdw().until_not.assert_called_with(
                            ec.text_to_be_present_in_element_value(), 
                                               '')

    def test_frame_to_be_available_and_switch_to_it(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.frame_to_be_available_and_switch_to_it(
                                    tag_name='warrior', timeout = 17)

                wdw.assert_called_with(driver = self.driver, timeout = 17)
                ec.frame_to_be_available_and_switch_to_it.assert_called_with(
                                    (By.TAG_NAME, 'warrior'))
                wdw().until_not.assert_called_with(
                            ec.frame_to_be_available_and_switch_to_it(), 
                                               '')
    
    def test_invisibility_of_element_located(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.invisibility_of_element_located(
                                    (By.ID, 'priest'), timeout = 17)

                wdw.assert_called_with(driver = self.driver, timeout = 17)
                ec.invisibility_of_element_located.assert_called_with(
                                    (By.ID, 'priest'))
                wdw().until_not.assert_called_with(
                            ec.invisibility_of_element_located(), 
                                               '')
    
    def test_element_to_be_clickable(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.element_to_be_clickable(
                                    (By.ID, 'lol'), timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.element_to_be_clickable.assert_called_with(
                                    (By.ID, 'lol'))
                wdw().until_not.assert_called_with(
                            ec.element_to_be_clickable(), 
                                               '')

    def test_staleness_of(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.staleness_of(self, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.staleness_of.assert_called_with(self)
                wdw().until_not.assert_called_with(
                            ec.staleness_of(), 
                                               '')

    def test_element_to_be_selected(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.element_to_be_selected(self, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.element_to_be_selected.assert_called_with(self)
                wdw().until_not.assert_called_with(
                            ec.element_to_be_selected(), 
                                               '')

    def test_element_located_to_be_selected(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.element_located_to_be_selected(class_ = 'ddy', 
                                                    timeout = 21)

                wdw.assert_called_with(driver = self.driver, timeout = 21)
                ec.element_located_to_be_selected.assert_called_with(
                                    (By.CLASS_NAME, 'ddy'))
                wdw().until_not.assert_called_with(
                            ec.element_located_to_be_selected(), 
                                               '')

    def test_element_selection_state_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.element_selection_state_to_be(self, 'up!')

                wdw.assert_called_with(driver = self.driver, timeout = 10)
                ec.element_selection_state_to_be.assert_called_with(
                                    self, 'up!')
                wdw().until_not.assert_called_with(
                            ec.element_selection_state_to_be(), 
                                               '')

    def test_element_located_selection_state_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.element_located_selection_state_to_be(
                                                    class_name = 'jalopnik',
                                                    state = 'down!',
                                                    timeout = 23)

                wdw.assert_called_with(driver = self.driver, timeout = 23)
                ec.element_located_selection_state_to_be.assert_called_with(
                                    (By.CLASS_NAME, 'jalopnik'), 'down!')
                wdw().until_not.assert_called_with(
                            ec.element_located_selection_state_to_be(), 
                                               '')

    def test_number_of_windows_to_be(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.number_of_windows_to_be(111, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.number_of_windows_to_be.assert_called_with(111)
                wdw().until_not.assert_called_with(
                            ec.number_of_windows_to_be(), 
                                               '')

    def test_new_window_is_opened(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.new_window_is_opened(111, timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.new_window_is_opened.assert_called_with(111)
                wdw().until_not.assert_called_with(
                            ec.new_window_is_opened(), 
                                               '')

    def test_alert_is_present(self):
        with patch('genie.webdriver.wait.WebDriverWait') as wdw:
            with patch('genie.webdriver.wait.EC') as ec:
                wait = WaitUntilNot(driver = self.driver, timeout = 10)
                wait.alert_is_present(timeout = 19)

                wdw.assert_called_with(driver = self.driver, timeout = 19)
                ec.alert_is_present.assert_called_with()
                wdw().until_not.assert_called_with(
                            ec.alert_is_present(), 
                                               '')
