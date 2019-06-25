
from selenium import webdriver

from pyats.connections import BaseConnection


class WebDriverConnector(BaseConnection):

    def __init__(self, *args, **kwargs):
        '''__init__

        instantiate a single connection instance.
        '''

        # instantiate parent BaseConnection
        super().__init__(*args, **kwargs)

        self.driver = None


    def connect(self):

        # do nothing if already connected
        if self.connected:
            return

        # get all connection information
        connection_info = self.connection_info.copy()

        # remove credentials block if present
        credentials = connection_info.pop('credentials', None)

        # rename ip -> host, cast to str type
        try:
            driver = connection_info.pop('driver')
            driver = getattr(webdriver, driver)

        except KeyError:
            raise ValueError('Missing driver: definition in YAML connection '
                             'section') from None

        except AttributeError:
            raise ValueError('No such driver type: %s' % driver) from None

        # remove class
        connection_info.pop('class')

        # create class
        self.driver = driver(**connection_info)

    def disconnect(self):
        self.driver.quit()

    @property
    def connected(self):
        try:
            return bool(self.driver.title) or True
        except Exception:
            return False

    def __getattr__(self, attr):
        # redirect get attribute to self.driver
        if hasattr(self.driver, attr):
            return getattr(self.driver, attr)
        else:
            raise AttributeError("'%s' object has no attribute '%s" 
                                 % (type(self).__name__, attr))

    def __dir__(self):
        return sorted(super().__dir__() + dir(self.driver))

    @property
    def execute(self):
        # chain this execute to driver's execute
        return self.driver.execute

    def configure(self, *args, **kwargs):
        raise RuntimeError("'%s' class does not support configure command" 
                           % type(self).__name__)
