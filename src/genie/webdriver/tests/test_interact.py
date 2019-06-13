import unittest
from unittest.mock import patch, Mock

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Test_Interact(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global Interactions

        from genie.webdriver.interact import Interactions

    def setUp(self):
        self.driver = Mock()

    def test_init(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            self.assertEqual(interact.timeout, 10)
            self.assertIs(interact.driver, self.driver)

            wait.assert_called_with(self.driver, 10)

        interact = Interactions(driver = self.driver, timeout = 10)

        from genie.webdriver.wait import Wait
        self.assertTrue(isinstance(interact.wait, Wait))

    def test_click_on_svg_element(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.click_on_svg_element(css = 'boomshakalala')
            self.driver.execute_script.assert_called_with(
            '''var ev = document.createEvent("SVGEvents");
                 ev.initEvent("click",true,true);
                 var target = $("boomshakalala").get(0);
                 target.dispatchEvent(ev);''')

    def test_click_button_with_text(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.click_button_with_text(text = 'boomshakalala')
            self.driver.execute_script.assert_called_with(
            '''return $('button:contains("boomshakalala")').click()''')

    def test_click_link_with_text(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.click_link_with_text(text = 'kaboom')
            self.driver.find_element_by_link_text.assert_called_with('kaboom')
            self.driver.find_element_by_link_text().click.assert_called_with()

    def test_type_in_active_input_element(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.type_in_active_input_element("iamgenius")
            self.driver.switch_to.active_element.send_keys.assert_called_with(
                                                      'iamgenius' + Keys.RETURN)

    def test_double_click(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            with patch('genie.webdriver.interact.ActionChains') as ac:
                interact = Interactions(driver = self.driver, timeout = 10)
                interact.double_click(object)

                ac.assert_called_with(self.driver)
                ac().double_click.assert_called_with(object)
                ac().double_click().perform.assert_called_with()

        with patch('genie.webdriver.wait.Wait') as wait:
            with patch('genie.webdriver.interact.ActionChains') as ac:
                self.driver.find_element.return_value = 'boomyeah!'
                interact = Interactions(driver = self.driver, timeout = 10)
                interact.double_click(id='tomhanks')

                self.driver.find_element.assert_called_with((By.ID, 'tomhanks'))
                ac.assert_called_with(self.driver)
                ac().double_click.assert_called_with('boomyeah!')
                ac().double_click().perform.assert_called_with()

    def test_hover(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            with patch('genie.webdriver.interact.ActionChains') as ac:
                interact = Interactions(driver = self.driver, timeout = 10)
                interact.hover(object)

                ac.assert_called_with(self.driver)
                ac().move_to_element.assert_called_with(object)
                ac().move_to_element().perform.assert_called_with()

        with patch('genie.webdriver.wait.Wait') as wait:
            with patch('genie.webdriver.interact.ActionChains') as ac:
                interact = Interactions(driver = self.driver, timeout = 10)
                interact.hover(object, x_offset=1, y_offset=2)

                ac.assert_called_with(self.driver)
                ac().move_to_element_with_offset.assert_called_with(object,1, 2)
                ac().move_to_element_with_offset().perform.assert_called_with()

        with patch('genie.webdriver.wait.Wait') as wait:
            with patch('genie.webdriver.interact.ActionChains') as ac:
                self.driver.find_element.return_value = 'boomyeah!'
                interact = Interactions(driver = self.driver, timeout = 10)
                interact.hover(id='tomhanks')

                self.driver.find_element.assert_called_with((By.ID, 'tomhanks'))
                ac.assert_called_with(self.driver)
                ac().move_to_element.assert_called_with('boomyeah!')
                ac().move_to_element().perform.assert_called_with()

    def test_select_from_drop_down(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            wait().until.visibility_of_element_located.return_value = (By.ID, 
                                                                 'tomhanks')
            with patch('genie.webdriver.interact.Select') as sel:
                interact = Interactions(driver = self.driver, timeout = 10)
                interact.select_from_drop_down('abc', id='tomhanks')

                sel.assert_called_with((By.ID, 'tomhanks'))
                sel().select_by_visible_text.assert_called_with('abc')

    def test_type_and_enter(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.type_and_enter(value = 'boomshakalala', id='100')
            wait().until.visibility_of_element_located.assert_called_with(
                                                       (By.ID, '100'))
            wait().until.visibility_of_element_located().send_keys.\
                            assert_called_with('boomshakalala', Keys.RETURN)

        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.type_and_enter(locator = '100', value = 'boomshakalala')
            wait().until.visibility_of_element_located.assert_called_with('100')
            wait().until.visibility_of_element_located().send_keys.\
                                assert_called_with('boomshakalala', Keys.RETURN)

    def test_send_return(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.send_return(id='100')
            wait().until.visibility_of_element_located.assert_called_with(
                                                       (By.ID, '100'))
            wait().until.visibility_of_element_located().send_keys.\
                                assert_called_with(Keys.RETURN)

        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.send_return(locator = '100')
            wait().until.visibility_of_element_located.assert_called_with('100')
            wait().until.visibility_of_element_located().send_keys.\
                                assert_called_with(Keys.RETURN)

    def test_send_tab(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.send_tab(id='100')
            wait().until.visibility_of_element_located.assert_called_with(
                                                       (By.ID, '100'))
            wait().until.visibility_of_element_located().send_keys.\
                                        assert_called_with(Keys.TAB)

        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.send_tab(locator = '100')
            wait().until.visibility_of_element_located.assert_called_with('100')
            wait().until.visibility_of_element_located().send_keys.\
                                    assert_called_with(Keys.TAB)

    def test_drag_and_drop(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            with patch('genie.webdriver.interact.ActionChains') as ac:
                interact = Interactions(driver = self.driver, timeout = 10)
                interact.drag_and_drop('abc', 'def')
                self.assertEqual(
                         wait().until.visibility_of_element_located.call_count,
                            2)

                ac().drag_and_drop().perform.assert_called_with()

    def test_drag_and_drop_element(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            with patch('genie.webdriver.interact.ActionChains') as ac:
                interact = Interactions(driver = self.driver, timeout = 10)
                interact.drag_and_drop_element('abc', 'def')

                ac().drag_and_drop.assert_called_with('abc', 'def')
                ac().drag_and_drop().perform.assert_called_with()

    def test_scroll_into_view(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            wait().until.visibility_of_element_located.return_value = 'lalala'
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.scroll_into_view(css = 'boomshakalala')
            self.driver.execute_script.assert_called_with(
            "arguments[0].scrollIntoView(true);", 'lalala')

        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.scroll_into_view(element = 'boomshakalala')
            self.driver.execute_script.assert_called_with(
            "arguments[0].scrollIntoView(true);", 'boomshakalala')

        with patch('genie.webdriver.wait.Wait') as wait:
            wait().until.visibility_of_element_located.return_value = 'jb'
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.scroll_into_view(locator = object)
            self.driver.execute_script.assert_called_with(
            "arguments[0].scrollIntoView(true);", 'jb')

    def test_jquery_click(self):
        with patch('genie.webdriver.wait.Wait') as wait:
            interact = Interactions(driver = self.driver, timeout = 10)
            interact.jquery_click(css = 'boomshakalala')
            self.driver.execute_script.assert_called_with(
            "$('boomshakalala').click()")
