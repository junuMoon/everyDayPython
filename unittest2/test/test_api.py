import unittest
import json
from app import app


class TestAPI(unittest.TestCase):

    def test_ner_endpoint_returns_200(self):
        with app.test_client() as client:
            response = client.post('ner')
            assert response.status_code == 200

    def test_ner_endpoint_returns_200_given_data(self):
        with app.test_client() as client:
            data = {'data': 'sample'}
            response = client.post('ner', json=data)
            assert response.status_code == 200

    def test_ner_endpoint_get_data_from_post_with_json(self):
        with app.test_client() as client:
            data = {'data': 'sample'}
            response = client.post('ner', json=data)
            return_data = response.get_data().decode('ascii')
            self.assertEqual(return_data, 'sample')

