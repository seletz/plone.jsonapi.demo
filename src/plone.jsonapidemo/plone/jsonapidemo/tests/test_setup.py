# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from plone.jsonapidemo.tests.base import IntegrationTestCase
from plone import api

import unittest2 as unittest


class TestInstall(IntegrationTestCase):
    """Test installation of plone.jsonapidemo into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_product_installed(self):
        """Test if plone.jsonapidemo is installed in portal_quickinstaller."""
        installer = api.portal.get_tool('portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('plone.jsonapidemo'))

    def test_uninstall(self):
        """Test if plone.jsonapidemo is cleanly uninstalled."""
        installer = api.portal.get_tool('portal_quickinstaller')
        installer.uninstallProducts(['plone.jsonapidemo'])
        self.assertFalse(installer.isProductInstalled('plone.jsonapidemo'))



def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

