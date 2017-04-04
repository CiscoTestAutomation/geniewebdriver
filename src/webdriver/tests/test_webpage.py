import unittest
from unittest.mock import patch, Mock

from selenium.webdriver.common.by import By

class Test_WebPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global WebPage

        from webdriver import WebPage
    
    def setUp(self):
        self.driver = Mock()

    def test_init(self):
        with patch('webdriver.wait.Wait') as wait:
            with patch('webdriver.interact.Interactions') as interact:
                
                class TestPage(WebPage):
                    URL = '/lol'
                
                page = TestPage(self.driver)

                self.assertEqual(page.timeout, 10)
                self.assertIs(page.driver, self.driver)
                wait.assert_called_with(self.driver, 10)
                interact.assert_called_with(self.driver, 10)
                self.assertEqual(page.url, '/lol')

                page = TestPage(self.driver, base_url = 'http://mock_url/')
                self.assertEqual(page.url, 'http://mock_url/lol')

    def test_redirect_and_dir(self):
        with patch('webdriver.wait.Wait') as wait:
            with patch('webdriver.interact.Interactions') as interact:
                
                class TestPage(WebPage):
                    URL = '/testpage'


                page = TestPage('abc')

                self.assertIn('startswith', dir(page))
                self.assertTrue(hasattr(page, 'endswith'))

    def test_open(self):
        with patch('webdriver.wait.Wait') as wait:
            with patch('webdriver.interact.Interactions') as interact:
                
                class TestPage(WebPage):
                    URL = '/testpage'


                page = TestPage(self.driver)
                page.open()

                self.driver.get.assert_called_with(page.url)

    def test_context_manager(self):
        with patch('webdriver.wait.Wait') as wait:
            with patch('webdriver.interact.Interactions') as interact:
                
                class TestPage(WebPage):
                    URL = '/testpage'

                
                with TestPage(self.driver) as page:
                    self.driver.get.assert_called_with(page.url)

    def test_find_element(self):
        with patch('webdriver.wait.Wait') as wait:
            with patch('webdriver.interact.Interactions') as interact:
                
                class TestPage(WebPage):
                    URL = '/testpage'

                page = TestPage(self.driver)

                page.find_element(id = 'name')

                self.driver.find_element.assert_called_with(By.ID, 'name')

                page.find_element([1,2])
                self.driver.find_element.assert_called_with(1,2)

    def test_find_elements(self):
        with patch('webdriver.wait.Wait') as wait:
            with patch('webdriver.interact.Interactions') as interact:
                
                class TestPage(WebPage):
                    URL = '/testpage'

                page = TestPage(self.driver)

                page.find_elements(id = 'name')

                self.driver.find_elements.assert_called_with(By.ID, 'name')

                page.find_elements([1,2])
                self.driver.find_elements.assert_called_with(1,2)