#! /bin/env python

'''Setup file for Libs

See:
    https://packaging.python.org/en/latest/distributing.html
'''

import os
import re
import sys

from ciscodistutils import setup, find_packages, is_devnet_build
from ciscodistutils.tools import read, find_version, generate_cython_modules
from ciscodistutils.common import SUPPORT, LICENSE, URL
from ciscodistutils.common import (AUTHOR,
                                   URL,
                                   CLASSIFIERS,
                                   SUPPORT,
                                   LICENSE,
                                   STD_EXTRA_REQ)




# generate package dependencies
install_requires = ['selenium']


# launch setup
setup(
    name = 'genie.webdriver',
    version = find_version('src', 'genie', 'webdriver', '__init__.py'),

    # descriptions
    description = 'A collection of tools and base classes intended to '
                  'simplify and standardize how automation engineers '
                  'develop Selenium based libraries',
    long_description = read('DESCRIPTION.rst'),

    # the project's main homepage.
    url = URL,

    # author details
    author = AUTHOR,
    author_email = SUPPORT,

    # project licensing
    license = LICENSE,

    # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=CLASSIFIERS,

    # project keywords
    keywords = 'genie pyats test automation webdriver',

    # uses namespace package
    namespace_packages = ['genie'],

    # project packages
    packages = find_packages(where = 'src'),

    # project directory
    package_dir = {
        '': 'src',
    },

    # additional package data files that goes into the package itself
    package_data = {
    },


    # console entry point
    entry_points = {
    },

    # package dependencies
    install_requires = install_requires,

    # any additional groups of dependencies.
    # install using: $ pip install -e .[dev]
    extras_require = STD_EXTRA_REQ,

    # external modules
    ext_modules = [],

    # any data files placed outside this package.
    # See: http://docs.python.org/3.4/distutils/setupscript.html
    # format:
    #   [('target', ['list', 'of', 'files'])]
    # where target is sys.prefix/<target>
    data_files = [],

    # non zip-safe (never tested it)
    zip_safe = False,
)
