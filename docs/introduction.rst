Introduction
============

`Selenium WebDriver`_ is a set of infrastructure, library and standards that 
allows end user to drive a web browser to act, respond and behave exactly as a
*user would* either locally or remotely. In the recent years, This has become
the de-facto standard for testing webpage/UI.

Typical usage of Selenium involves using a language binding, such as `Selenium 
Python Bindings`_, and connect to a web browser through either local browser
driver, or via remote selenium server:

- Google Chrome browser: ChromeDriver_
- Firefox browser: GeckoDriver_
- Remote Server: `Selenium Server`_

Through this language binding, the user would then be able to make various calls
to the browser for selecting various UI elements, emulating key strokes, mouse
clicks, etc, and in turn, automate the testing of web pages and web UIs.

.. code-block:: python
    
    # Example
    # -------
    #
    # the simplest selenium script
    #   - using pure selenium webdriver python binding
    #   - connects to google.com and perform a search on selenium

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome()
    driver.get('http://www.google.com')

    assert 'Google' in driver.title

    elem = driver.find_element_by_class_name('gsfi')
    
    elem.clear()
    elem.send_keys('Selenium WebDriver')
    elem.send_keys(Keys.RETURN)

    driver.close()

Goal
----

The goal of this WebDriver package is not to replace any of the above. Rather, 
its intention is to translate the above 'raw' coding methods into more fluid, 
object-oriented coding paradigms, and offer base classes, guidelines and 
examples on building extendable libraries for websites under test. 

In addition, this package also optionally enables users to treat a web browser 
under the pyATS topology/device architecture, and connects to a browser in their
test scripts by defining the connection methods under their testbed YAML file.

This package is thus useable for straight Selenium testing under test harnesses
such ass Py.test, Python unittest, etc, as well as through pyATS.

Benefits
--------

This packages enables pyATS users to write Selenium web page automation code and
leverage all the feature benefits of core pyATS infrastructure, namely:

- using YAML testbed file to abstract out the need to hard-code web browser
  driver details

- using `connection methodology`_ to support multiple simultaneous driver
  instance, windows & sessions, including adding them to a connection pool and 
  performing actions in a distributed fashion.

- take advantage of concurrency_
  
  - running multiple test scripts in parallel through Easypy

  - using Pcall to run tests, functions etc, synchronously

- build agnostic library infrastructure using Cisco-Shared `abstract`_ package,
  allowing the library to handle minute differences between page revisions 
  through tokens.

- mix & match feature tests with selenium tests: fulfilling the need to test
  Cisco DNA/SDN architecture, and being able to intermix both northbound and
  southbound tests together in one test suite.

.. _connection methodology: http://wwwin-pyats.cisco.com/documentation/latest/connections/index.html
.. _concurrency: http://wwwin-pyats.cisco.com/documentation/latest/async/index.html
.. _abstract: http://wwwin-pyats.cisco.com/cisco-shared/abstract/html/


Prerequisite
------------

Users of this package is expected to at least understand the fundamentals of how
Selenium works, how to resolve their environment issues w.r.t. starting their
instance of browser/driver/server, and how to use the native Python bindings 
effectively. 

Keep in mind that this package is here to only simplifies and standize the usage
of Selenium and not to replace it. As such, users still need to train themselves
on how to properly setup/use selenium.


Installation & Examples
-----------------------

This package is featured on the pyATS Cisco internal PyPI server. To install in
regular pyATS environments, simply do the following in your environment:

.. code-block:: bash

    pip install webdriver

This package also works outside of pyATS. If you want to leverage this package 
in any other straight-up Python environment, try the following:

.. code-block:: bash

    pip install --index-url http://pyats-pypi.cisco.com/simple webdriver

This package wraps core functionality from `Selenium Python Bindings` package. 
As such, on installation, it will also install ``selenium`` package from Python
PyPI.

After installation, basic examples for using this package will be installed to
your Python virtual environment under ``$VIRTUAL_ENV/examples/webdriver`` 
folder.

Dependencies
------------

Keep in mind that in order for the bindings to instanciate a web browser,
the corresponding driver needs to be part of your environment ``PATH``,
or provided as argument to the init:

.. code-block:: python

    # Example
    # -------
    #
    #   firefox browser bindings

    from selenium import webdriver

    # Firefox will try to lookup 'geckodriver' in your PATH
    # (this is required for running firefox browser locally in Linux)
    driver = webdriver.Firefox()

    # or you can provide the driver executable path directly
    driver = webdriver.Firefox('/path/to/geckodriver')

In addition, each version of selenium and browser driver only works with a range
of given browser versions. Getting latest/greatest driver/browser combination to
work in Linux is sometimes quite challenging (especially in Cisco CEL servers).
This is outside the scope of this support document - this package deals with 
boilerplate code, base classes and guidelines, whereas starting the browser is a
trivial part of understanding how-to-use Selenium. 

Support
-------

For issues & questions related to this package, please use Piestack: 
http://piestack.cisco.com. 


.. _Selenium WebDriver: http://www.seleniumhq.org/projects/webdriver/
.. _Selenium with Python: http://selenium-python.readthedocs.io/index.html
.. _ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/
.. _GeckoDriver: https://github.com/mozilla/geckodriver/releases
.. _Selenium Server: http://selenium-python.readthedocs.io/installation.html#downloading-selenium-server
.. _Selenium Python Bindings: http://selenium-python.readthedocs.io/