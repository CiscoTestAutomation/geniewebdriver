import unittest

from selenium.webdriver.common.by import By

class Test_Translator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global kwarg_to_locator, translate_arguments
        global translate_args_with_passthru
        
        from genie.webdriver.utils import (
            kwarg_to_locator, 
            translate_arguments,
            translate_args_with_passthru
        )

    def test_internal_translation(self):
        expectations = dict(id = (By.ID, 'value'),
                            xpath = (By.XPATH, 'value'),
                            link = (By.LINK_TEXT, 'value'),
                            link_text = (By.LINK_TEXT, 'value'),
                            partial_link = (By.PARTIAL_LINK_TEXT, 'value'),
                            partial_link_text = (By.PARTIAL_LINK_TEXT, 'value'),
                            name = (By.NAME, 'value'),
                            tag = (By.TAG_NAME, 'value'),
                            tag_name = (By.TAG_NAME, 'value'),
                            class_ = (By.CLASS_NAME, 'value'),
                            class_name = (By.CLASS_NAME, 'value'),
                            css = (By.CSS_SELECTOR, 'value'),
                            css_selector = (By.CSS_SELECTOR, 'value'))

        for name, expected in expectations.items():
            obj = kwarg_to_locator(**{name:'value'})
            self.assertEqual(obj, expected)

    def test_internal_translation_corner_case(self):
        with self.assertRaises(ValueError):
            kwarg_to_locator()

        with self.assertRaises(ValueError):
            kwarg_to_locator(css = 'value', tag = 'name')

        with self.assertRaises(ValueError):
            kwarg_to_locator(a=1, b=2)

    def test_translate_arguments(self):
        expectations = dict(id = (By.ID, 'value'),
                            xpath = (By.XPATH, 'value'),
                            link = (By.LINK_TEXT, 'value'),
                            link_text = (By.LINK_TEXT, 'value'),
                            partial_link = (By.PARTIAL_LINK_TEXT, 'value'),
                            partial_link_text = (By.PARTIAL_LINK_TEXT, 'value'),
                            name = (By.NAME, 'value'),
                            tag = (By.TAG_NAME, 'value'),
                            tag_name = (By.TAG_NAME, 'value'),
                            class_ = (By.CLASS_NAME, 'value'),
                            class_name = (By.CLASS_NAME, 'value'),
                            css = (By.CSS_SELECTOR, 'value'),
                            css_selector = (By.CSS_SELECTOR, 'value'))

        for name, expected in expectations.items():
            obj = translate_arguments(**{name:'value'})
            self.assertEqual(obj, expected)

            obj = translate_arguments(expected)            
            self.assertEqual(obj, expected)

    def test_translate_arguments_corner_case(self):
        with self.assertRaises(ValueError):
            kwarg_to_locator()

        with self.assertRaises(ValueError):
            translate_arguments(css = 'value', tag = 'name')

        with self.assertRaises(ValueError):
            translate_arguments(a=1, b=2)

        with self.assertRaises(ValueError):
            translate_arguments((By.ID, 'value'), id='value')

    def test_translate_arguments_args_n_kwargs(self):
        args = ((By.ID, 'value'),)
        kwargs = {}
        self.assertEqual((By.ID, 'value'), translate_arguments(*args, **kwargs))

        args = ()
        kwargs = dict(css = 'boom')
        self.assertEqual((By.CSS_SELECTOR, 'boom'), 
                         translate_arguments(*args, **kwargs))

    def test_translate_args_with_passthru(self):
        expectations = dict(id = (By.ID, 'value'),
                            xpath = (By.XPATH, 'value'),
                            link = (By.LINK_TEXT, 'value'),
                            link_text = (By.LINK_TEXT, 'value'),
                            partial_link = (By.PARTIAL_LINK_TEXT, 'value'),
                            partial_link_text = (By.PARTIAL_LINK_TEXT, 'value'),
                            name = (By.NAME, 'value'),
                            tag = (By.TAG_NAME, 'value'),
                            tag_name = (By.TAG_NAME, 'value'),
                            class_ = (By.CLASS_NAME, 'value'),
                            class_name = (By.CLASS_NAME, 'value'),
                            css = (By.CSS_SELECTOR, 'value'),
                            css_selector = (By.CSS_SELECTOR, 'value'))

        for name, expected in expectations.items():
            obj, remainder = translate_args_with_passthru(**{name:'value', 
                                                             name+'1':'boo'})
            self.assertEqual(obj, expected)
            self.assertEqual(remainder, {name+'1':'boo'})

            obj, remainder = translate_args_with_passthru(expected, 
                                                          **{name+'1':'boo'})
            self.assertEqual(obj, expected)
            self.assertEqual(remainder, {name+'1':'boo'})

    def test_translate_args_with_passthru_corner_case(self):
        with self.assertRaises(ValueError):
            translate_args_with_passthru()

        with self.assertRaises(ValueError):
            translate_args_with_passthru(css = 'value', tag = 'name')

        with self.assertRaises(ValueError):
            translate_args_with_passthru(a=1, b=2)

        with self.assertRaises(ValueError):
            translate_args_with_passthru((By.ID, 'value'), id='value')
