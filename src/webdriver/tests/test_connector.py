import unittest
from unittest.mock import patch, Mock, MagicMock

try:
    from ats import topology
except ImportError:
    topology = None

class Test_WebDriverConnector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global WebDriverConnector

        from webdriver import WebDriverConnector

    @unittest.skipIf(topology is None, "missing topology module")
    def test_init_from_yaml(self):
        yaml = '''
devices:
    dummy:
        type: something
        connections:
            chrome:
                class: webdriver.WebDriverConnector
                driver: Chrome
'''
        with patch('webdriver.connectors.webdriver') as wbd:
            tb = topology.loader.load(yaml)
            self.assertEqual(
                tb.devices['dummy'].connections.chrome['class'].__name__,
                'WebDriverConnector')

    def test_init(self):
        class Dummy(): pass
        device = Dummy()
        with patch('webdriver.connectors.webdriver') as wbd:
            conn = WebDriverConnector(device = device, 
                                      alias = 'dummy',
                                      via = 'boom')

            self.assertEqual(conn.driver, None)
            self.assertEqual(conn.alias, 'dummy')
            self.assertEqual(conn.via, 'boom')

    def test_connect(self):
        class Dummy(): pass
        device = Dummy()
        device.connections = dict()
        device.connections['boom'] = {
            'driver':'Chrome',
            'chrome_options': '111',
            'class': 'webdriver.WebDriverConnector',
        }


        with patch('webdriver.connectors.webdriver') as wbd:
            wbd.Chrome().service.process.poll.return_value = None

            conn = WebDriverConnector(device = device, 
                                      alias = 'dummy',
                                      via = 'boom')


            conn.connect()
            wbd.Chrome.assert_called_with(chrome_options = '111')
            self.assertTrue(isinstance(conn.driver, MagicMock))
            self.assertIs(conn.connected, True)

    def test_argument_chain(self):
        class Dummy(): pass
        device = Dummy()
        device.connections = dict()
        device.connections['boom'] = {
            'driver':'Chrome',
            'chrome_options': '111',
            'class': 'webdriver.WebDriverConnector',
        }


        with patch('webdriver.connectors.webdriver') as wbd:
            wbd.Chrome().service.process.poll.return_value = None

            conn = WebDriverConnector(device = device, 
                                      alias = 'dummy',
                                      via = 'boom')


            conn.connect()
            self.assertEqual(conn.execute, conn.driver.execute)
            self.assertEqual(conn.assert_called_with, 
                             conn.driver.assert_called_with)

    def test_configure(self):
        class Dummy(): pass
        device = Dummy()
        device.connections = dict()
        device.connections['boom'] = {
            'driver':'Chrome',
            'chrome_options': '111',
            'class': 'webdriver.WebDriverConnector',
        }


        with patch('webdriver.connectors.webdriver') as wbd:
            wbd.Chrome().service.process.poll.return_value = None

            conn = WebDriverConnector(device = device, 
                                      alias = 'dummy',
                                      via = 'boom')

            with self.assertRaises(RuntimeError):
                conn.configure('blah')