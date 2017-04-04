from webdriver import (PageElement, TextBox, Button, RadioButton, 
                               Checkbox, Selector, WebPage)


class TestPage(WebPage):

    drop_down = Selector(name='abc')
    text_box_1 = TextBox(value = 'Mickey')
    text_box_2 = TextBox(value = 'Mouse')

    submit_button = Button(tag = 'button')

    radio_button_1 = RadioButton(value = 'male')
    radio_button_2 = RadioButton(value = 'female')
    radio_button_3 = RadioButton(value = 'other')

    check_box_1 = Checkbox(value = 'Bike')
    check_box_2 = Checkbox(value = 'Car')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/ws/siyuan-ott/selenium/cisco-shared/webdriver/chromedriver.cel6')


driver.get('file:///ws/siyuan-ott/selenium/cisco-shared/webdriver/src/webdriver/tests/test.html')

page = TestPage(driver)

import code; code.interact(local = locals())

page.text_box_1 = 'pyats is'
page.text_box_2 = 'awesome'

selector = page.drop_down
selector.select_by_visible_text('Opel')

print(page.radio_button_1, page.radio_button_2, page.radio_button_3)

page.radio_button_2 = True

print(page.check_box_1, page.check_box_2)
page.check_box_1 = True
page.check_box_1 = False
