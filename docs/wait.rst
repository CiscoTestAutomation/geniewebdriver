Wait Object
===========

To a human user, waiting for web pages to load, for UI interactions to take time
and watching page animations comes as a natural, subconscious thing: it's part 
of the overall experience of surfing. 

However, in the case of automation, the automation script (Selenium code) can
run magnitudes faster than the browser loading the actual web page, making 
locating elements difficult. This is further exacerbated by the use of 
multi-threaded  loading in different browers, and AJAX techniques within each
web page implementation.

To properly code this interactive experience using automation, users needs to 
use ``Wait()`` objects: implicitly wait x seconds, or explicitly wait & poll for
a UI element to become ready. The Selenium Python bindings provides this 
`wait functionality`_ in a crude fashion. 

.. _wait functionality: http://selenium-python.readthedocs.io/waits.html

This ``webdriver`` features a higher-level implementation that stream lines this
experience: ``webdriver.wait.Wait`` class combines Selenium low-level wait apis
and expected conditions into a single structure, where method calls and 
attribute chains depics what the user wants to do.

.. code-block:: python

    # Example
    # -------
    #
    #   straight up selenium vs this package's implementation

    # standard webdriver isntance
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get("http://somedomain/url_that_delays_loading")


    # in straight/standard selenium, to wait for an element
    # the following code is needed.
    # -----------------------------------------------------------------
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )


    # this package wraps this in a better mechanism
    # -----------------------------------------------------------------
    from genie.webdriver.wait import Wait

    wait = Wait(driver, 10)
    element = wait.until.presence_of_element_located(id = 'myDynamicElement')

The ``webdriver.wait.Wait()`` object is instantiated with the following 
arguments:
    
.. code-block:: text
    
    Format
    ------
        Wait(driver, timeout)

    Where
    -----
        driver: the provided driver (or device connector)
        timeout: default timeout for all wait conditions under this instance

.. hint::
    
    once a ``Wait()`` object is created, you can keep reusing it. 


Implicit Wait
-------------

An implicit wait simply instructs the driver to poll the DOM for certain amount
of time.

.. code-block:: python
    
    # Example
    # -------
    #
    #   implicit waits

    from genie.webdriver.wait import Wait

    # assume we have a driver
    # and a default wait timer of 30s
    wait = Wait(driver, timeout = 30)

    # wait for 10 seconds
    wait(10)

    # if no timeout value is provided on call, 
    # it waits for the default amount.
    wait()      # wait 30s


Explicit Waits
--------------

An explicit wait is a case where the code explicitly polls/waits for a condition
to occur before moving forward. All current explicit wait and conditions are 
wrapped in ``webdriver.wait.Wait`` class, allowing for shorthand use.

.. code-block:: text

    Format
    ------

        Wait().[until|until_not].<condition>([value],
                                             locator|locator_kwargs,
                                             [timeout], [message], [poll_frequency],
                                             [ignored_exceptions])

    Where
    -----
        [value]: provided expected condition value (only if applicable)
        locator|locator_kwargs: locator tuple or kwargs (see locator documentation)
        [timeout]: specific timeout for this expected condition
        [message]: message to display/throw if condition is not met
        [poll_frequency]: sleep interval between polls, default to 0.5s
        [ignored_exceptions]: iterable structure of exception classes ignored during
                              calls. By default, it contains NoSuchElementException 
                              only.


.. code-block:: python
    
    # Example
    # -------
    #
    #   explicit waits

    from genie.webdriver.wait import Wait

    # assume we have a driver
    # with a default timeout of 10s
    wait = Wait(driver, timeout = 10)


    # wait until title is "my title page"
    # eg, equivalent to raw selenium
    #   WebDriverWait(driver, 10).until(EC.title_is('my title page'))
    wait.until.title_is('my title page')
    
    # wait until title is no longer "my title page"
    # (in addition, poll every 1 second for 30s, with specific error message)
    # eg, equivalent to raw selenium
    #   WebDriverWait(driver, 10, 1).until_not(EC.title_is('my title page'),
                                               'page title did not change')
    wait.until_not.title_is('my title page',
                            timeout = 30,
                            message = 'page title did not change',
                            poll_frequency = 1)

    # wait for element to be clickable, where element ID = someid
    # eg, equivalent to raw selenium
    #   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,
    #                                                               'someid')))
    wait.until.element_to_be_clickable(id = 'someid')

In otherwords, the ``Wait()`` class chains together the condition to the poll
mechanism as attribute chains.

- ``Wait().until`` waits until the following method condition is met
- ``Wait().until_not`` is the inverse of above.

The following is the list of available condition methods to be used with the
above. Note that the optional arguments ``timeout``, ``poll_frequency``, 
``message`` and ``ignored_exceptions`` are not shown in the api input for
simplicity - they are applicable/useable as optional kwargs in all of them.

``.title_is(title)``
    condition where the page title matches to the input text


``.title_contains(text)``
    condition where the page title contains the above text

``.presence_of_element_located(locator)``
    condition where the given element (described by locator) is found.
    Returns the element object

``.visibility_of_element_located(locator)``
    condition where the given element (described by locator) is found and is
    visible in the current page. Returns the element object

``.visibility_of(element)``
    condition where the given element object is visible in the current page

``.presence_of_all_elements_located(locator)``
    An expectation for checking that there is at least one element present on a
    web page. Returns list of element found

``.visibility_of_any_elements_located(locator)``
    An expectation for checking that there is at least one element visible on 
    a web page. Returns list of element found

``.text_to_be_present_in_element(text, locator)``
    An expectation for checking if the given text is present in the
    specified element (described by locator).

``.text_to_be_present_in_element_value(text, locator)``
    An expectation for checking if the given text is present in the element's 
    value (element specified by locator)

``.frame_to_be_available_and_switch_to_it(locator)``
    An expectation for checking whether the given frame is available to
    switch to.  If the frame is available it switches the given driver to the
    specified frame.

``.invisibility_of_element_located(locator)``
    An Expectation for checking that an element is either invisible 
    or not present on the DOM.

``.element_to_be_clickable(locator)``
    An expectation for checking an element (described by locator) is visible 
    and enabled such that you can click it. 

``.staleness_of(element)``
    Condition where an element is no longer attached to the DOM.

``.element_to_be_selected(element)``
    condition for checking the given element is selected

``.element_located_to_be_selected(locator)``
    condition for checking the given element (described by locator) is selected.

``.element_selection_state_to_be(element, state)``
    An expectation for checking if the given element is of the provided selected
    state

``.element_located_selection_state_to_be(locator, state)``
    An expectation for checking if the given element (described by locator) is 
    of the provided selected state

``.number_of_windows_to_be(num_windows)``
    An expectation for the number of windows to be a certain value.

``.new_window_is_opened(current_handles)``
    An expectation that a new window will be opened and have the number of
    windows handles increase.

``.alert_is_present()``
    Expects an alert to be present.
