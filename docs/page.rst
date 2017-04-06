WebPage Design Pattern
======================

Selenium Python bindings introduced the concept of `Page Design Pattern`_. It 
augments the Selenium web element object model by introducing the concept of
modeling each web page as a ``Page()`` class, and present interesting page
elements (such as input boxes, buttons) using class attributes, more 
importantly, `Python Descriptor`_ attributes.

This ``webdriver`` package takes this design pattern to the next level, and 
introduces the standard base classes ``WebPage()`` and ``PageElement()``. 
These allows all web page automation libraries to look & feel the same, 
following the same set of design concepts and implementation, reusing where
applicable.


WebPage Class
-------------

Base class for all web page libraries to inherit from. Each class represents
a web page, given a particular URL. This allows the library developer to 
aggregate page elements, actions & verifications onto a single object, using
methods and attribute to represent interactions and form values. Features:

- builds page URLs based on a base url and supports value substitution
- :doc:`wait` and :doc:`interact` are both automatically added to class
- can be used as a context manager using ``with`` statement.
- wraps ``find_element()`` and ``find_elements()`` api with locator kwargs
  support.
- redirect known calls (such as ``find_element_by_name()``) at class level to
  driver automatically.

.. code-block:: python

    # Example
    # -------
    #
    #   a page representing www.google.com search actions

    from webdriver import WebPage
    from webdriver.element import TextBox

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
                                      search_string = text.replace(' ', '+'))

        def verify_title(self):
            # wait until title is loaded
            return self.wait.until.title_is('Google')

    class GoogleSearchResult(WebPage):
        
        # result page requires a search string
        # use string substution syntax
        # this will automatically get filed by __init__(search_string = '...')
        URL = '/?q={search_string}'

        # ... etc

    # --------------------------------------------------------------------------

    # using the above code is very straight forward
    # (let's use straight webdriver for example)
    from selenium import webdriver

    driver = webdriver.Firefox()
    google_home = 'http://www.google.com'

    # instanciate page
    page = GoogleSearch(driver, base_url = google_home)

    # open the page (nagivate to page)
    page.open()
    page.verify_title()

    # search for something
    page.search('python is awesome')

    # or use it as a context manager:
    with GoogleSearch(driver, google_home) as page:
        page.search('python is so awesome')
        page.find_element_by_link_text('Help')

    # boom

The above code makes use of the infrastructure provided in ``WebPage()`` class,
and as well uses the PageElement_ to facilitate represent page content.

.. csv-table:: WebPage() class __init__ Arguments
    :header: "Name", "Description"
    :widths: 30, 100

    ``driver``,"driver or pyATS device with connector acting as driver"
    ``base_url``, "the base website url where this page's specific URL buils on"
    ``timeout``, "default wait timeout value in seconds for this page's elements"
    ``**urlkwargs``, "keyword-arguments to be used to fullfill the URL template 
    through string substition"

All ``WebPage()`` subclasses needs to define its unique ``URL`` attribute. This
stores the relative url this page represents. Upon instantiation, any 
``**urlkwargs`` provided to ``WebPage().__init__()`` will be used as 
string-substituion kwargs input to the URL, if provided.

.. code-block:: python

    # Example
    # -------
    #   
    #   url substitution

    class GoogleSearchResult(WebPage):
        
        URL = '/?q={search_string}'

    # would be init as:
    page = GoogleSearchResult(driver, 'http:://www.google.com', 
                              search_string='python+string+substitution')

    # eg, the page.url would be:
    page.url
    # http://www.google.com/?q=python+string+substitution

This automatic URL building mechanism is defined at ``WebPage().build_url()``
method, and can be further modified by subclasses. For example, in the above 
example, the search page had to do a string subsitution from space to ``+`` to
"encode" the search string into proper page string. This need would be avoided
altogether if ``GoogleSearchResult()`` had it own builder that overrides the
default string substitution, adding logic to handle these conditions.

.. csv-table:: WebPage Default Attributes/Methods
    :header: "Name", "Description"
    :widths: 30, 100

    ``URL``, "string representing URL of this page. Supports string subsitution"
    ``url``, "url combining the base url and this page's specific url"
    ``base_url``, "the provided base website url"
    ``driver``, "the provided driver object"
    ``timeout``, "default timeout for this page's elements, default to 10s"
    ``urlkwargs``, "any other kwargs provided to __init__()"
    ``wait``, ":doc:`wait` auto-created for this page"
    ``interact``, ":doc:`interact` auto-created for this page"
    ``open()``, "open this webpage based on self.url"
    ``find_element()``, "wrapper to driver.find_element() api, supporting 
    also locator kwargs argument" 
    ``find_elements()``, "wrapper to driver.find_elements() api, supporting 
    also locator kwargs argument"
    ``build_url()``, "api called by __init__() to build the page url based on
    urlkwargs input"


.. _PageElement:

PageElement Class
-----------------

The ``PageElement`` class further simplifies defining and locating page elements
by combining a page element locator, its getter and setter functionality (which
can be customized to suit the given element), into a `Python Descriptor`_. 
``PageElement`` classes are designed to solely work with ``WebPage()`` classes,
and can take advantage of their built-in :doc:`wait` and :doc:`interact`.

The simplest ``PageElement`` instance describes web page element by some sort
of locator:

.. code-block:: python

    # Example
    # -------
    #
    #   page element example

    # keep in mind that this needs to work with WebPage class
    from webdriver import WebPage
    from webdriver.element import PageElement

    class LoginPage(WebPage):

        URL = '/login'

        # define the username box:
        username_box = PageElement(id = 'username-id')

        # define the password box
        password_box = PageElement(id = 'passwd-id')

        # define the login button
        login_button = PageElement(id = 'Login')

        # define the "remember me"
        remember_me = PageElement(id = 'remember_me')

The use of descriptor protocol allows the page instance to automatically gain
the ability to retrieve page elements through attributes:

.. code-block:: python

    # ... continuing the above example

    page = LoginPage(driver, base_url = 'http://somewebsite/'

    # use the elements
    # PageElement returns the element object by locator
    page.username_box.send_keys('my_username')
    page.password_box.send_keys('my_password')

    # set remember_me
    if not page.remember_me.is_selected():
        page.remember_me.click()

    # click login button
    page.login_button.click()

In essense, ``PageElement`` class allows the user to wrap most commonly used 
logic around getting & setting web page elements into python descriptor protocol
``__set__()`` and ``__get__`` methods. The ``PageElement()`` class provides the
basic getter based on the provided locator. Subclasses can therefore built on
top and add more functionality.

This page includes the following subclasses for intuitive use:

``webdriver.element.TextBox(locator or value)``
    defines a text box input element using locator, locator kwargs, or a value.
    If value is provided, uses the predefined XPATH search pattern: 
    ``.//input[@type='text' and @value='{value}']`` to locate element. 
    ``GET`` returns the current text box value, and ``SET`` automatically types 
    text into the box. 

``webdriver.element.Button(locator)``
    defines a button element using locator or locator kwargs.
    ``GET`` returns the element object when the button becomes "clickable"

``webdriver.element.RadioButton(locator or value)``
    defines a radio button input element using locator, locator kwargs, or a 
    value. If value is provided, uses the predefined XPATH search pattern: 
    ``.//input[@type='radio' and @value='{value}']`` to locate element. 
    ``GET`` returns the current radio button state (true for selected, false 
    not), and ``SET`` accepts true/false value to set/unset the radio button.

``webdriver.element.Checkbox(locator or value)``
    defines a checkbox input element using locator, locator kwargs, or a 
    value. If value is provided, uses the predefined XPATH search pattern: 
    ``.//input[@type='checkbox' and @value='{value}']`` to locate element. 
    ``GET`` returns the current checkbox value (true for selected, false not), 
    and ``SET`` accepts true/false value to check/uncheck the box.

``webdriver.element.Selector(locator)``
    defines a drop down selector using locator or locator kwargs. ``SET``
    returns a ``selenium.webdriver.support.ui.Select`` object instance.

Using these subclasses, we can further refactor the above ``LoginPage`` as:

.. code-block:: python

    # Example
    # -------
    #
    #   refactoring login page using subclass of PageElements

    # keep in mind that this needs to work with WebPage class
    from webdriver import WebPage
    from webdriver.element import Button, TextBox, Checkbox

    class LoginPage(WebPage):

        URL = '/login'

        # define the username box:
        username_box = TextBox(id = 'username-id')

        # define the password box
        password_box = TextBox(id = 'passwd-id')

        # define the login button
        login_button = Button(id = 'Login')

        # define the "remember me checkbox"
        remember_me = Checkbox(id = 'remember_me')


    # and the usage pattern becomes much more intuitive

    page = LoginPage(driver, base_url = 'http://somewebsite/'

    # use the elements
    # PageElement returns the element object by locator
    page.username_box = 'my_username'
    page.password_box = 'my_password'
    page.remember_me = True

    # click login button
    page.login_button.click()

.. hint::

    you are encouraged to make contributions to page elements to benefit the
    user communit :-)

.. _Page Design Pattern: http://selenium-python.readthedocs.io/page-objects.html

.. _Python Descriptor: https://docs.python.org/3.4/howto/descriptor.html