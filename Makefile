################################################################################
#                                                                              #
#                      Cisco Systems Proprietary Software                      #
#        Not to be distributed without consent from Test Technology            #
#                               Cisco Systems, Inc.                            #
#                                                                              #
################################################################################
#                            WebDriver Internal Makefile
#
# Author:
#   Siming Yuan    (siyuan)    - CSG
#
# Support:
#	python-core@cisco.com
#
# Version:
#   v1.0
#
# Date: 
#   April 2017
#
# About This File:
#   This script will build the webdriver package for distribution in PyPI server
#
# Requirements:
#	1. Module name is the same as package name.
#	2. setup.py file is stored within the module folder
################################################################################

# Variables
PKG_NAME      = webdriver
BUILDDIR      = $(shell pwd)/__build__
PROD_USER     = pyadm@pyats-ci
PROD_PKGS     = /auto/pyats/packages/cisco-shared
PYTHON        = python
TESTCMD       = python -m unittest discover -f tests/
DISTDIR       = $(BUILDDIR)/dist

.PHONY: clean package distribute develop undevelop help\
        docs distribute_docs test

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "package         : Build the package"
	@echo "test            : Test the package"
	@echo "distribute      : Distribute the package to PyPi server"
	@echo "clean           : Remove build artifacts"
	@echo "develop         : Set package to development mode"
	@echo "undevelop       : Unset the package from development mode"
	@echo "docs             : Build Sphinx documentation for this package"

test:
	@$(TESTCMD)

docs:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Building $(PKG_NAME) documentation for preview: $@"
	@echo ""

	@./setup.py docs

	@echo "Completed building docs for preview."
	@echo ""

package:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Building $(PKG_NAME) distributable: $@"
	@echo ""

	@./setup.py test
	@mkdir -p $(DISTDIR)

    # NOTE : Only specify --universal if the package works for both py2 and py3
    # https://packaging.python.org/en/latest/distributing.html#universal-wheels
	@./setup.py bdist_wheel --universal --dist-dir=$(DISTDIR)

	@echo "Completed building: $@"
	@echo ""

develop:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Building and installing $(PKG_NAME) development distributable: $@"
	@echo ""

	@./setup.py develop --no-deps -q

	@echo "Completed building and installing: $@"
	@echo ""

undevelop:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Uninstalling $(PKG_NAME) development distributable: $@"
	@echo ""

	@./setup.py develop --no-deps -q --uninstall

	@echo "Completed uninstalling: $@"
	@echo ""

clean:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Removing make directory: $(BUILDDIR) ..."
	@rm -rf $(BUILDDIR)
	@echo ""
	@echo "Removing build artifacts ..."
	@./setup.py clean
	@echo ""
	@echo "Done."

distribute:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Copying all distributable to $(PROD_PKGS)"
	@test -d $(DISTDIR) || { echo "Nothing to distribute! Exiting..."; exit 1; }
	@ssh -q $(PROD_USER) 'test -e $(PROD_PKGS)/$(PKG_NAME) || mkdir $(PROD_PKGS)/$(PKG_NAME)'
	@scp $(DISTDIR)/* $(PROD_USER):$(PROD_PKGS)/$(PKG_NAME)
	@echo ""
	@echo "Done."
	@echo ""
