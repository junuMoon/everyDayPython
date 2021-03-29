import unittest
import json
from flask import request

from app import app


class TestApi(unittest.TestCase):

    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Steven Malkom is in a good band"})
            assert response._status_code == 200

    def test_ner_endpoint_given_json_body_with_known_entities_returns_entity_result_in_response(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Steven Malkom"})
            data = json.loads(response.get_data())

            assert data['entities'][0]['ent'] == 'Steven Malkom'
            assert data['entities'][0]['label'] == 'Person'

    # def test_ner_endpoint_given_json_body_with_known_entities_returns_html_result_in_response(self):
        # with app.test_client() as client:
        #     response = client.post('/ner', json={"sentence": "Steven Malkom"})
        #     data = json.loads(response.get_data())
        #
        #     self.assertEqual(data.get('html'), result_html)