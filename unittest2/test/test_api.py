import unittest
import json
from flask import Request
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

    def test_ner_endpoint_return_json_from_post_with_json(self):
        with app.test_client() as client:
            data = {'data': 'sample'}
            response = client.post('ner', json=data)
            return_data = response.get_data().decode('ascii')
            return_data = json.loads(return_data)
            self.assertEqual(return_data.get('data'), 'sample')

    def test_ner_endpoint_nerModel_return_json(self):
        with app.test_client() as client:
            sent = 'Kim lives in Madrid.'
            sent_dict = {'sentence': sent}
            response = client.post('ner', json=sent_dict)
            data = response.get_json().get('ents')
            expected_result = [
                {'Kim': 'Person'},
                {'Madrid': 'Location'}
            ]
            self.assertEqual(data, expected_result)


    # def test_home_return_200_from_request_with_json(self):
    #     with app.test_client() as client:
    #         data = {'ents':[
    #             {'Kim': 'Person'},
    #             {'Madrid': 'Location'}
    #         ]}
    #         response = client.get('/', json=data)
    #
    #         assert response.status_code == 200

    # def test_home_return_json_from_get_request_of_ner_route(self):
    #     with app.test_client() as client:
    #         data = {'ents':[
    #             {'Kim': 'Person'},
    #             {'Madrid': 'Location'}
    #         ]}