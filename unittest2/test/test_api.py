import unittest
from flask import template_rendered, request
from contextlib import contextmanager
from app import app


@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.test_app = app.test_client()

    def test_ner_endpoint_returns_200_to_get_request(self):
        response = self.test_app.get('/')
        assert response.status_code == 200

    def test_ner_endpoint_returns_200_to_post_request_with_form_content_type_given_empty_sentence(self):
        data = {'sentence': ''}
        response = self.test_app.post('/', data=data, content_type="application/x-www-form-urlencoded")
        assert response.status_code == 200

    def test_ner_endpoint_returns_200_to_post_request_with_form_content_type_given_nonempty_sentence(self):
        data = {'sentence': 'Kim lives in Madrid'}
        response = self.test_app.post('/', data=data, content_type="application/x-www-form-urlencoded")
        assert response.status_code == 200