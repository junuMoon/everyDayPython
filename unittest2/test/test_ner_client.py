import unittest
from ner_client import NerClient


class TestNerClient(unittest.TestCase):

    def test_ner_client_returns_dictionary_given_empty_sent(self):
        model = NerClient()
        sent = ''
        ents = model.get_ents(sent)
        self.assertIsNotNone(ents)
