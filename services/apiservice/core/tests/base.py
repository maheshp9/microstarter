
from flask_testing import TestCase
from core import create_app

app = create_app()

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('core.config.TestingConfig')
        return app

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
