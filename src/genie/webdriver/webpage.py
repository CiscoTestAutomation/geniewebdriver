from urllib.parse import urljoin
from . import utils, wait, interact

DEFAULT_TIMEOUT = 10

class WebPage(object):

    @property
    def URL(self):
        raise NotImplementedError('Must set page URL when subclassing')

    def __init__(self, 
                 driver, 
                 base_url = None, 
                 timeout = DEFAULT_TIMEOUT,
                 **urlkwargs):
        self.driver = driver
        self.timeout = timeout
        self.wait = wait.Wait(self.driver, timeout)
        self.interact = interact.Interactions(self.driver, timeout)
        self.base_url = base_url
        self.urlkwargs = urlkwargs

        self.url = self.build_url()

    def build_url(self):
        return urljoin(self.base_url, self.URL.format(**self.urlkwargs))

    def __getattr__(self, attr):
        # redirect get attribute to self.driver
        if hasattr(self.driver, attr):
            return getattr(self.driver, attr)
        else:
            raise AttributeError("'%s' object has no attribute '%s" 
                                 % (type(self).__name__, attr))

    def __dir__(self):
        return sorted(super().__dir__() + dir(self.driver))

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator = None, **kwargs):
        locator = utils.translate_arguments(locator, **kwargs)

        return self.driver.find_element(*locator)

    def find_elements(self, locator = None, **kwargs):
        locator = utils.translate_arguments(locator, **kwargs)

        return self.driver.find_elements(*locator)

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        return