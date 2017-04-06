Interaction Object
==================

This package also includes an ``Interactions()`` class that automates the most 
commonly-used boilerplate interactive actions web automation needs into simple
method calls.

.. code-block:: python

    # Example
    # -------
    #
    #   using interaction class

    from webdriver.interact import Interactions

    # given a driver... and a default interaction timeout of 10s
    interaction = Interactions(driver, 10)

    # we can perform common interactions directly
    # without invoking complex api calls.
    interaction.click_button_with_text('submit')
    interaction.click_link_with_text('link to documentation')
    interaction.double_click(id = 'login_check')
    interaction.type_and_enter('today is a good day', tag = 'input')


``Interactions.click_on_svg_element(css)``
    click on an SVG element in the webpage, locating it using the provided css
    selector value.

``Interactions.click_button_with_text(text)``
    click on button that contains a particular text string

``Interactions.click_link_with_text(text)``
    click on link that matches up with given text string.

``Interactions.type_in_active_input_element(text)``
    switch to active element and input text in it, and press ENTER.

``Interactions.double_click(element, locator)``
    double click the provided element (or element defined by the locator), 
    and double click it.

``Interactions.hover(element, locator, [x_offset], [y_offset])``
    move and hover mouse over element (or element defined by locator) center. If
    offsets are provided, hover over the offset area (offset from top left 
    corner)

``Interactions.select_from_drop_down(option, locator)``
    select the provided option text a drop down menu, found using the given
    locator.

``Interactions.type_and_enter(value, locator)``
    find element by locator, and type given value/text in it, and press ENTER.

``Interactions.send_return(locator)``
    find element by locator, and press ENTER.

``Interactions.send_tab(locator)``
    find element by locator, and press TAB.

``Interactions.drag_and_drop(source, dest)``
    action chain: drag a given source element (found by locator) to destination 
    element (found by locator)

``Interactions.drag_and_drop_element(source, dest)``
    action chain: drag a given source element to destination element

``Interactions.scroll_into_view(element, locator)``
    scroll the page until the provided element or element found by locator is
    in the current view.

``Interactions.jquery_click(css)``
    perform a jquery click on provided css selector element


