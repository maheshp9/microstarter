import json
import unittest

from core.tests.base import BaseTestCase

class TestApiService(BaseTestCase):

    def test_entities(self):
        response = self.client.get('/api/entities/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data['status'])


if __name__ == '__main__'
    unittest.main()