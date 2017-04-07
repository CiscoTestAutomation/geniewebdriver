from ats import aetest

from libs import google

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_browser(self, testbed, browser):
        
        # get device
        driver = testbed.devices[browser]

        # connect via webdriver
        driver.connect(via = 'webdriver')

        # save to paramters
        self.parent.parameters['driver'] = driver



class TestSearch(aetest.Testcase):
    '''Test case that opens search page and performs a search, expecting
    some sort of page result'''

    @aetest.setup
    def setup(self, driver, base_url):

        # create page object instance
        self.page = google.GoogleSearch(driver = driver, timeout = 10,
                                        base_url = base_url)

        # open the page
        self.page.open()

    @aetest.test
    def test_search(self):
        self.page.search('google is awesome')

        self.page.wait.until.title_contains('Google Search')

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_browser(self, driver):
        
        driver.destroy()