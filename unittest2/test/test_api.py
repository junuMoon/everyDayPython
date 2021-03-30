import unittest
from app import app

class TestAPI(unittest.TestCase):

    def test_app_has_homepage(self):
        with app.test_client() as client:
            self.assertIsNotNone(client.title)

