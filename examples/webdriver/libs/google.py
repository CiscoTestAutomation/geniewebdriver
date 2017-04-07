from webdriver import WebPage
from webdriver.element import TextBox, Button

from urllib.parse import urljoin, quote


class GoogleSearch(WebPage):

    # relative url from the base url
    # (disabling auto-complete for easier demo automation)
    URL = '/webhp?complete=0'

    # define the search box
    search_box = TextBox(class_ = 'gsfi')

    # define the search button
    search_button = Button(name = 'btnK')

    # define the feeling lucky button
    lucky_button = Button(name = 'btnI')

    def search(self, text, lucky = False):
        # put text into search box
        self.search_box = text

        # click search button
        if lucky:
            self.lucky_button.click()
        else:
            self.search_button.click()

        # because the above action redirects to a new page, it may be worth
        # considering returning a new page object.
        return GoogleSearchResult(self.driver, self.base_url,
                                  search_string = text)

    def verify_title(self):
        # wait until title is loaded
        return self.wait.until.title_is('Google')

class GoogleSearchResult(WebPage):

    # result page requires a search string
    # use string substution syntax
    # this will automatically get filed by __init__(search_string = '...')
    URL = '/?q={search_string}'

    def build_url(self):

        # quote the given string
        text = self.urlkwargs.get('search_string', '')
        text = quote(text)

        return urljoin(self.base_url, self.URL.format(search_string = text))
