Navigation & Location
=====================

The most fundamental part of web automation is to nagivate a page, find elements
fill in forms and click on buttons. This ``webdriver`` package does not modify
the original intuitiness of the navigation concept/apis. The only functionality
it adds is to be able to locate elements using keyword-argument style instead of
the default locator tuple.


Native Concepts
---------------

Call the ``get`` method of a driver to open a particular webpage.

.. code-block:: python

    driver.get('http://www.google.com')

Call ``find_element_*()`` apis to find page DOM elements (WebElement object), 
and sending keys

.. code-block:: python
    
    element = driver.find_element_by_id("passwd-id")
    element = driver.find_element_by_name("passwd")
    element = driver.find_element_by_xpath("//input[@id='passwd-id']")

    element.send_keys("some text")

    element.send_keys(" and some", Keys.ARROW_DOWN)
    element.send_keys("some text")
    
    element.clear()

Filling in forms:

.. code-block:: python

    element = driver.find_element_by_xpath("//select[@name='name']")
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        print("Value is: %s" % option.get_attribute("value"))
        option.click()

    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element_by_name('name'))
    select.select_by_index(index)
    select.select_by_visible_text("text")
    select.select_by_value(value)

    select = Select(driver.find_element_by_id('id'))
    select.deselect_all()

    driver.find_element_by_id("submit").click()

    element.submit()

Etc... these functionality remain unchanged. See `Navigating`_ documentation 
for details.

.. _Navigating: http://selenium-python.readthedocs.io/navigating.html#navigating


Locator Kwarg Concept
---------------------

In Selenium Python bindings, when a **locator** is provided as input to
a function, it typically comes in a *tuple* format, describing a DOM location 
*by something*.

.. code-block:: python

    # Example
    # -------
    #
    #   native python binding locator

    from selenium.webdriver.common.by import By

    # locator is a tuple of (By.<type>, 'value')
    locator = (By.ID, 'id_to_look_for')

    # available By's
    By.ID                   # locate by id attribute of element
    By.NAME                 # locate by the name attribute of element
    By.XPATH                # using XPath language to find element in XHTML
    By.LINK_TEXT            # locate by link text string in anchor tag
    By.PARTIAL_LINK_TEXT    # locate by partial link text string in anchor tag
    By.TAG_NAME             # locate by html tag name
    By.CLASS_NAME           # locate by element class attribute name
    By.CSS_SELECTOR         # locate by element CSS selector syntax

This format is used throughout the native python binding implementation, 
expecially with waits and expected conditions. It could be quite cumbersome to 
use, given its syntax and specificness:

.. code-block:: python
    
    # note the usage of the locator tuple
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )

Instead of mandating a locator tuple all the time, this ``webdriver`` package
introduces the concept of using keyword-arguments to depict location in addition
to the native locator tuple. We call this the **locator kwarg**.

.. code-block:: text

    Mapping By.<type> To Locator Keyword Argument
    ---------------------------------------------

    (By.ID, 'value')                 id = 'value'
    (By.Name, 'name')                name = 'name'
    (By.XPATH, 'path')               xpath = 'path'
    (By.LINK_TEXT, 'text')           link = 'text' or link_text = 'text'
    (By.PARTIAL_LINK_TEXT, 'text')   partial_link = 'text' or partial_link_text = 'text'
    (By.TAG_NAME, 'tagname')         tag = 'tag_name' or tag_name = 'tagname'
    (By.CLASS_NAME, 'classname'      class_ = 'classname' or class_name = 'classname'
    (By.CSS_SELECTOR, 'cssvalue')    css = 'cssvalue' or css_selector = 'cssvalue'

.. code-block:: python

    # Example
    # -------
    #
    #   using locator kwargs interchageably within this package
    #   (and using webdriver.wait.Wait() class as example)

    # the traditional tuple format is doable
    from selenium.webdriver.common.by import By
    wait.until.element_to_be_clickable((By.ID, 'some_element_id'))
    wait.until.element_to_be_clickable((By.XPATH, "//input[@name='continue'][@type='button']"))

    # or use the locator kwarg format
    wait.until.element_to_be_clickable(id = 'some_element_id')
    wait.until.element_to_be_clickable((xpath = "//input[@name='continue'][@type='button']"))

This locator keyword-argument format is applicable to all APIs within this
package where a ``locator`` argument is expected.