import unittest
from ner_client import NerClient


class TestNerClient(unittest.TestCase):

    def test_ner_client_returns_dictionary_given_empty_sent(self):
        model = NerClient()
        sent = ''
        ents = model.get_ents(sent)
        self.assertIsNotNone(ents)

    def test_ner_clinet_returns_entities_dictionary_given_nonempty_sent(self):
        model = NerClient()
        sent = 'Franco lives in Madrid.'
        ents = model.get_ents(sent)
        expected_result = {
            'ents': [
                {'Franco': 'Person'},
                {'Madrid': 'Location'}
            ]
        }
        self.assertEqual(ents, expected_result)