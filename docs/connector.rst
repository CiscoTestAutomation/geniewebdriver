Drivers & Connectors
====================

The core concept of Selenium revolves around using a **driver** to manipulate 
web browsers to do stuff. This package maps driver functionality into that of
pyATS testbed/device model, enabling users to use native drivers, and pyATS
topology/device/connection modelled drivers to work interchangeably.

.. note::

    for all intents and purposes, throughout this document, when a ``driver``
    is referenced, it can be either a selenium driver instance, or a pyATS
    connector instance. The package works with both, interchangeably.


Driver Instance
---------------

In Python Selenium bindings, a driver is an object instance that translates 
method calls into corresponding browser automation actions. This is the basis to
all Selenium testing. 

.. code-block:: python

    # Example
    # -------
    #
    #   instantiating a browser driver

    from selenium import webdriver

    # create a Chrome driver
    driver = webdriver.Chrome()

The driver object is used throughout the infrastructure from there on to perform
various actions such as finding elements, waiting for elements, performing
clicks, etc.


pyATS Connector
---------------

In pyATS test methodology, testbeds and devices are represented in YAML format
as defined in the topology_ module, and during runtime, loaded into object form.

The concept of a ``device`` in this context is quite generic: it could be used
to represent any piece of "equipment" used during testing. This means that we 
could model a web browser as a device when performing Selenium testing:

- the 'method' of connecting to this browser would be defined under 
  ``connections:`` block of this device

- each connection instance represents a single browser window

Together, this allows pyATS test scripts to use the traiditional YAML testbed
standard to decouple the need to "hard-code" browser connection definitions, and
abstract out the test library code itself. This is conceptually similar to how
scripts should be able to run on multiple testbeds with the same topology.

This ``genie.webdriver`` package defines the connector implementation
``genie.webdriver.connectors.WebDriverConnector`` required to adapt a pyATS topology
device object to corresponding web browser driver.

.. code-block:: yaml

    # Example
    # -------
    #
    #   pyATS testbed yaml example for defining a selenium browser under device

    testbed:
        name: example_selenium_testbed

    devices:
        firefox:                            # this is a firefox browser
            type: browser
            connections:
                webdriver:
                    # specify the driver connector class
                    class: genie.webdriver.connectors.WebDriverConnector
                    driver: Firefox
                    executable_path: '/path/to/firefox/geckodriver'

                    # optional arguments below
                    firefox_profile: null
                    firefox_binary: null
                    timeout: 30
                    capabilities: null
                    proxy: null
                    firefox_options: null

        chrome:                             # this is a chrome browser
            type: browser
            connections:
                webdriver:
                    class: genie.webdriver.connectors.WebDriverConnector
                    driver: Chrome
                    executable_path: /path/to/chromedriver

                    # optional arguments below
                    port: null
                    chrome_options: null
                    service_args: null
                    desired_capabilities: null
                    service_log_path: null

With the above definition, the testbed loader can then load this YAML into
object form.

.. code-block:: python

    # Example
    # -------
    #
    #   loading & using selenium testbed yaml file in pyATS and 

    # import the topology module
    from pyats import topology

    # load the above testbed file containing selenium drivers
    testbed = topology.loader.load('/path/to/selenium/testbed.yaml')

    # get device by name
    # (in this case, a browser)
    device = testbed.devices['chrome']

    # connect to it 
    # (eg, open browser driver/session)
    device.connect(via = 'webdriver')

    # execute any driver apis
    # (note that device here is really, a driver)
    element = device.find_element_by_id("passwd-id")
    element = device.find_element_by_name("passwd")
    element = device.find_element_by_xpath("//input[@id='passwd-id']")

    element.send_keys("some text")

    # etc..

In essence, the ``genie.webdriver.connectors.WebDriverConnector`` is a pyATS
`connection class`_ implementation that converts YAML connection specifications
into an actual Selenium Driver instance. All arguments/options defined under 
the connection definition is converted into that driver's ``__init__()`` 
argument. For example, see `ChromeDriver documentation`_.

After connection, the ``device`` object modeling a selenium driver gains all
the driver's abilities and APIs, as defined in the `binding documentation`_. Any
method call to the native driver class should be also callable under this 
device instance. 

.. hint::
    
    The device object, when used with this selenium connector class, is designed
    to behave exactly like the original Selenium driver instance it replaced.
    Therefore, for all intents and purposes, this object should be treated and
    used no differently than the above, base driver. 

    .. code-block:: python

        # Example
        # -------
        #
        #   using connector object with straight selenium objects

        # import the topology module
        from pyats import topology

        # load testbed, connect
        testbed = topology.loader.load('/path/to/selenium/testbed.yaml')
        device = testbed.devices['chrome']
        device.connect(via = 'webdriver')

        # rename it to driver to further confuse you :)
        driver = device

        # use it with the original selenium example
        # -----------------------------------------
        from selenium.webdriver.common.keys import Keys

        driver.get('http://www.google.com')

        assert 'Google' in driver.title

        elem = driver.find_element_by_class_name('gLFyf')
        
        elem.clear()
        elem.send_keys('Selenium WebDriver')
        elem.send_keys(Keys.RETURN)

        # remember to call disconnect() instead of close()
        driver.disconnect()

Options can be passed via testbed yaml like below:

.. code-block:: yaml

    devices:
        chrome:                             # this is a chrome browser
            type: browser
            connections:
                webdriver:
                    class: genie.webdriver.connectors.WebDriverConnector
                    driver: Chrome
                    options:
                        binary_location: '/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta'
                        headless: True

The same can be done by passing objects to device.connect() like below. This example passes both service and options.

.. code-block:: python

    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    
    option = Options()
    option.binary_location='/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta'
    
    service=Service(ChromeDriverManager(version='104.0.5112.20').install())
    
    device.connect(service=service, options=option)

.. _topology: http://wwwin-pyats.cisco.com/documentation/latest/topology/index.html

.. _connection class: http://wwwin-pyats.cisco.com/documentation/latest/connections/class.html

.. _binding documentation: http://selenium-python.readthedocs.io/locating-elements.html

.. _ChromeDriver documentation: http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.webdriver
