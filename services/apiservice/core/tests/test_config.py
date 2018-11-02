import os
import unittest

from flask import current_app
from flask_testing import TestCase

from core import create_app

app = create_app()

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('core.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(current_app is None)
        self.assertFalse(app.config['TESTING'])


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('core.config.TestingConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['TESTING'])
