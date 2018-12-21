from selenium.webdriver.common.by import By

# mapping for converting func(By.ID, 'value') to func(id = value)
LOCATOR_MAPPING = dict(id = By.ID,
                       xpath = By.XPATH,
                       link = By.LINK_TEXT,
                       link_text = By.LINK_TEXT,
                       partial_link = By.PARTIAL_LINK_TEXT,
                       partial_link_text = By.PARTIAL_LINK_TEXT,
                       name = By.NAME,
                       tag = By.TAG_NAME,
                       tag_name = By.TAG_NAME,
                       class_ = By.CLASS_NAME,
                       class_name = By.CLASS_NAME,
                       css = By.CSS_SELECTOR,
                       css_selector = By.CSS_SELECTOR)

LOCATOR_MAPPING_SET = set(LOCATOR_MAPPING.keys())


def kwarg_to_locator(**kwargs):
    '''basic function to translate id='name' style into (By.ID, 'name')

    Argument:
        kwargs: keyword value pair that gets translated. only one kwarg is 
                supported. 

    Returns:
        (By.<Type>, 'value')
    '''
    
    if not kwargs:
        raise ValueError('Nothing to convert - received no kwargs. Did you '
                         'provide a locator kwarg?')

    if len(kwargs) > 1:
        raise ValueError('Only supports converting a single kwarg to locator, '
                         'got: %s' % kwargs)

    # pick the only item in the list
    name, value = next(iter(kwargs.items()))

    if name not in LOCATOR_MAPPING:
        raise ValueError('Only supports convert the following keys: %s' %
                         list(LOCATOR_MAPPING.keys()))

    return LOCATOR_MAPPING[name], value

def translate_arguments(locator = None, **kwargs):
    '''function to either accept a locator object directly, or through a kwarg
    to be translated.

    Examples:
        translate_argument((By.ID, 'value'))
        translate_argument(id='value')

    Argument:
        locator: selenium locator style object
        kwargs: keyword value pair that gets translated. only one kwarg is 
                supported. 

    Returns:
        (By.<Type>, 'value')
    '''

    if not (locator or kwargs) or (locator and kwargs):
        raise ValueError('Must supply one argument at a time: either using '
                         'a locator directly, or use a kwarg for translation')

    return locator or kwarg_to_locator(**kwargs)

def translate_args_with_passthru(locator = None, **kwargs):
    input_set = set(kwargs.keys())

    if locator:
        # locator provided, check no duplicate arguments
        if LOCATOR_MAPPING_SET - input_set != LOCATOR_MAPPING_SET:
            raise ValueError("Cannot provie both 'locator' argument and use "
                             "the alternative kwargs shortcut form "
                             "together")

        return locator, kwargs

    # no locator, look for translation
    key = LOCATOR_MAPPING_SET & input_set

    if not key:
        raise ValueError("Must provide either a 'locator' or using the "
                         "alternative kwargs shortcut format")

    if len(key) > 1:
        raise ValueError("Only one locator kwarg form can be provided. Got:"
                         " %s" % list(key))

    # get the key
    key = next(iter(key))

    # convert locator kwarg to locator object
    locator = LOCATOR_MAPPING[key], kwargs.pop(key)

    return locator, kwargs