import unittest
from unittest.mock import Mock, patch

from selenium.webdriver.common.by import By


class Test_Element(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global PageElement, TextBox, Button, RadioButton, Checkbox, Selector
        from genie.webdriver.element import (
            PageElement, 
            TextBox, 
            Button, 
            RadioButton, 
            Checkbox, 
            Selector
        )

    def setUp(self):
        self.driver = Mock()

    def test_PageElement(self):
        class Dummy(Mock):
            pe = PageElement(id = 'abc')
            driver = self.driver

        obj = Dummy().pe
        self.driver.find_element.assert_called_with(By.ID, 'abc')

        class Dummy(Mock):
            pe = PageElement((By.ID, 'efg'))
            driver = self.driver
        obj = Dummy().pe
        self.driver.find_element.assert_called_with(By.ID, 'efg')

        with self.assertRaises(NotImplementedError):
            Dummy().pe = 1

    def test_TextBox_get(self):
        class Dummy(Mock):
            tb = TextBox(id = 'abc')
            wait = Mock()

        obj = Dummy().tb
        Dummy.wait.until.visibility_of_element_located.assert_called_with(
                                                             (By.ID, 'abc'))
        Dummy.wait.until.visibility_of_element_located().\
                            get_attribute.assert_called_with('value')

        class Dummy(Mock):
            tb = TextBox(value = 'xyz')
            wait = Mock()

        obj = Dummy().tb
        Dummy.wait.until.visibility_of_element_located.assert_called_with(
                (By.XPATH, ".//input[@type='text' and @value='xyz']"))
        Dummy.wait.until.visibility_of_element_located().\
                            get_attribute.assert_called_with('value')

        class Dummy(Mock):
            tb = TextBox(locator = object)
            wait = Mock()

        obj = Dummy().tb
        Dummy.wait.until.visibility_of_element_located.assert_called_with(
                     object)
        Dummy.wait.until.visibility_of_element_located().\
                            get_attribute.assert_called_with('value')

    def test_TextBox_set(self):
        class Dummy(Mock):
            tb = TextBox(id = 'abc')
            wait = Mock()

        Dummy().tb = 100
        Dummy.wait.until.visibility_of_element_located.assert_called_with(
                                                             (By.ID, 'abc'))
        Dummy.wait.until.visibility_of_element_located().\
                            clear.assert_called_with()
        Dummy.wait.until.visibility_of_element_located().\
                            send_keys.assert_called_with('100')

        class Dummy(Mock):
            tb = TextBox(value = 'xyz')
            wait = Mock()

        obj = Dummy().tb
        Dummy.wait.until.visibility_of_element_located.assert_called_with(
                (By.XPATH, ".//input[@type='text' and @value='xyz']"))
        Dummy.wait.until.visibility_of_element_located().\
                            get_attribute.assert_called_with('value')

        class Dummy(Mock):
            tb = TextBox(locator = object)
            wait = Mock()

        obj = Dummy().tb
        Dummy.wait.until.visibility_of_element_located.assert_called_with(
                     object)
        Dummy.wait.until.visibility_of_element_located().\
                            get_attribute.assert_called_with('value')


    def test_Button(self):
        class Dummy(Mock):
            bt = Button(id = 'abc')
            wait = Mock()

        bt = Dummy().bt
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                                                             (By.ID, 'abc'))


        with self.assertRaises(NotImplementedError):
            Dummy().bt = 1

    def test_RadioButton_get(self):
        class Dummy(Mock):
            rb = RadioButton(id = 'abc')
            wait = Mock()

        obj = Dummy().rb
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                                                             (By.ID, 'abc'))
        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.assert_called_with()

        class Dummy(Mock):
            rb = RadioButton(value = 'xyz')
            wait = Mock()

        obj = Dummy().rb
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                (By.XPATH, ".//input[@type='radio' and @value='xyz']"))
        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.assert_called_with()

        class Dummy(Mock):
            rb = RadioButton(locator = object)
            wait = Mock()

        obj = Dummy().rb
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                     object)
        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.assert_called_with()

    def test_RadioButton_set(self):
        class Dummy(Mock):
            rb = RadioButton(id = 'abc')
            wait = Mock()

        Dummy().rb = True
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                                                             (By.ID, 'abc'))
        Dummy.wait.until.element_to_be_clickable().\
                            click.assert_called_with()

        class Dummy(Mock):
            rb = RadioButton(value = 'xyz')
            wait = Mock()

        Dummy().rb = True
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                (By.XPATH, ".//input[@type='radio' and @value='xyz']"))
        Dummy.wait.until.element_to_be_clickable().\
                            click.assert_called_with()

        class Dummy(Mock):
            rb = RadioButton(locator = object)
            wait = Mock()

        Dummy().rb = True
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                     object)
        Dummy.wait.until.element_to_be_clickable().\
                            click.assert_called_with()

        class Dummy(Mock):
            rb = RadioButton(locator = object)
            wait = Mock()

        Dummy().rb = False
        self.assertEqual(Dummy.wait.until.element_to_be_clickable.call_count, 0)
        self.assertEqual(Dummy.wait.until.element_to_be_clickable().\
                            click.call_count, 0)

    def test_Checkbox_get(self):
        class Dummy(Mock):
            cb = Checkbox(id = 'abc')
            wait = Mock()

        obj = Dummy().cb
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                                                             (By.ID, 'abc'))
        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.assert_called_with()

        class Dummy(Mock):
            cb = Checkbox(value = 'xyz')
            wait = Mock()

        obj = Dummy().cb
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                (By.XPATH, ".//input[@type='checkbox' and @value='xyz']"))
        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.assert_called_with()

        class Dummy(Mock):
            cb = Checkbox(locator = object)
            wait = Mock()

        obj = Dummy().cb
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                     object)
        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.assert_called_with()

    def test_Checkbox_set(self):
        class Dummy(Mock):
            cb = Checkbox(id = 'abc')
            wait = Mock()

        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.return_value = False
        Dummy().cb = True
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                                                             (By.ID, 'abc'))
        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.assert_called_with()
        Dummy.wait.until.element_to_be_clickable().\
                            click.assert_called_with()

        Dummy.wait.until.element_to_be_clickable().\
                            click.reset_mock()
        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.return_value = True
        Dummy().cb = True
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                                                             (By.ID, 'abc'))
        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.assert_called_with()
        self.assertEqual(
                Dummy.wait.until.element_to_be_clickable().click.call_count, 0)

        Dummy.wait.until.element_to_be_clickable().\
                            click.reset_mock()

        Dummy().cb = False

        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.assert_called_with()
        Dummy.wait.until.element_to_be_clickable().\
                            click.assert_called_with()

        class Dummy(Mock):
            cb = Checkbox(id = 'abc')
            wait = Mock()

        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.return_value = False
        Dummy().cb = False
        Dummy.wait.until.element_to_be_clickable.assert_called_with(
                                                             (By.ID, 'abc'))
        Dummy.wait.until.element_to_be_clickable().\
                            is_selected.assert_called_with()
        self.assertEqual(
                Dummy.wait.until.element_to_be_clickable().click.call_count, 0)

    def test_Selector(self):
        with patch('genie.webdriver.element.Select') as selector_mock:
            class Dummy(Mock):
                selector = Selector(id = 'abc')
                wait = Mock()

            obj = Dummy().selector
            Dummy.wait.until.element_to_be_clickable.assert_called_with(
                                                                 (By.ID, 'abc'))
            selector_mock.assert_called_with(
                                    Dummy.wait.until.element_to_be_clickable())

            class Dummy(Mock):
                selector = Selector(object)
                wait = Mock()

            obj = Dummy().selector
            Dummy.wait.until.element_to_be_clickable.assert_called_with(object)

            with self.assertRaises(TypeError):
                Dummy().selector = 1
