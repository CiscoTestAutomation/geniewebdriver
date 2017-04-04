from webdriver import WebPage, TextBox, Button


class S3_LoginPage(WebPage):

    username_box = TextBox(name = 'username')
    password_box = TextBox(name = 'password')
    login_button = Button(class_ = 'btn')

    def __init__(self, driver):
        super().__init__(driver)

        # open page
        self.driver.get('http://aalfakhr-dev:8088/')

    def enter_credentials(self, username = None, password = None):
        if username:
            self.username_box = username

        if username:
            self.password_box = password

    def click_on_login_button(self):
        self.login_button.click()
        
    def login(self, username, password):
        self.enter_credentials(username, password)
        self.click_on_login_button()