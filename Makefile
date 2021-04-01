################################################################################
#                                                                              #
#                      Cisco Systems Proprietary Software                      #
#        Not to be distributed without consent from Test Technology            #
#                               Cisco Systems, Inc.                            #
#                                                                              #
################################################################################
#                            genie.webdriver Internal Makefile
#
# Author:
#   pyats-support@cisco.com
#
# Support:
#   pyats-support@cisco.com
#
# Version:
#   v2.0
#
# Date:
#   December 2018
#
# About This File:
#   This script will build the genie.webdriver package for
#   distribution in PyPI server
#
# Requirements:
#	1. Module name is the same as package name.
#	2. setup.py file is stored within the module folder
################################################################################

# Variables
PKG_NAME      = genie.webdriver
BUILD_DIR     = $(shell pwd)/__build__
DIST_DIR      = $(BUILD_DIR)/dist
STAGING_PKGS  = /auto/pyats/staging/packages
PYTHON        = python
TESTCMD       = ./tests/runAll --path=./tests/
BUILD_CMD     = $(PYTHON) setup.py bdist_wheel --dist-dir=$(DIST_DIR)
PYPIREPO      = pypitest
PROD_USER     = pyadm@pyats-ci

# Development pkg requirements
DEPENDENCIES  = restview psutil Sphinx wheel asynctest
DEPENDENCIES += setproctitle sphinx-rtd-theme
DEPENDENCIES += pip-tools

# Dependencies for building documentation
DOCS_DEPENDENCIES = Sphinx sphinxcontrib-napoleon sphinxcontrib-mockautodoc sphinx-rtd-theme


.PHONY: clean package distribute develop undevelop help devnet\
        docs test install_build_deps uninstall_build_deps install_build_deps \
		distribute_staging

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "package               Build the package"
	@echo "test                  Test the package"
	@echo "distribute            Distribute the package to internal Cisco PyPi server"
	@echo "distribute_staging    Distribute build pkgs to staging area"
	@echo "clean                 Remove build artifacts"
	@echo "develop               Build and install development package"
	@echo "undevelop             Uninstall development package"
	@echo "docs                  Build Sphinx documentation for this package"
	@echo "install_build_deps:     Install build dependencies for docs (will be run in make docs)"


html: docs

docs:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Building $(PKG_NAME) documentation for preview: $@"
	@echo ""

	sphinx-build -M html docs/ $(BUILD_DIR)/documentation

	@echo "Completed building docs for preview."

test:
	@$(TESTCMD)

uninstall_build_deps:
	@echo "no op"

install_build_deps:
	@echo "Installing build dependecies into your environment"
	@pip install $(DOCS_DEPENDENCIES)
	@echo ""
	@echo "Done"


package:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Building $(PKG_NAME) distributable: $@"
	@echo ""

	$(BUILD_CMD)

	@echo ""
	@echo "Completed building: $@"
	@echo ""
	@echo "Done."
	@echo ""

develop:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Building and installing $(PKG_NAME) development distributable: $@"
	@echo ""

	@pip install $(DEPENDENCIES)

	@$(PYTHON) setup.py develop --no-deps

	@pip install -e ".[dev]"

	@echo ""
	@echo "Completed building and installing: $@"
	@echo ""
	@echo "Done."
	@echo ""

undevelop:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Uninstalling $(PKG_NAME) development distributable: $@"
	@echo ""

	@$(PYTHON) setup.py develop --no-deps -q --uninstall

	@echo ""
	@echo "Completed uninstalling: $@"
	@echo ""
	@echo "Done."
	@echo ""

clean:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Removing make directory: $(BUILD_DIR)"
	@rm -rf $(BUILD_DIR) $(DIST_DIR)
	@echo ""
	@echo "Removing build artifacts ..."
	@$(PYTHON) setup.py clean
	@echo ""
	@echo "Done."
	@echo ""

distribute_staging:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Copying all distributable to $(STAGING_PKGS)"
	@test -d $(DIST_DIR) || { echo "Nothing to distribute! Exiting..."; exit 1; }
	@ssh -q $(PROD_USER) 'test -e $(STAGING_PKGS)/$(PKG_NAME) || mkdir $(STAGING_PKGS)/$(PKG_NAME)'
	@scp $(DIST_DIR)/* $(PROD_USER):$(STAGING_PKGS)/$(PKG_NAME)/
	@echo ""
	@echo "Done."
	@echo ""
