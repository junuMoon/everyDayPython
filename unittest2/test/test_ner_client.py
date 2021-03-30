import unittest
from ner_client import NerClient


class TestNerClient(unittest.TestCase):

    def test_ner_client_returns_empty_list_given_empty_sent(self):
        model = NerClient()
        sent = ''
        ents = model.get_ents(sent)
        self.assertIsInstance(ents, list)

    def test_ner_client_returns_entity_dictionary_list_given_multiple_known_entity_sent(self):
        model = NerClient()
        sent = 'Franco lives in Madrid.'
        ents = model.get_ents(sent)
        expected_result = [
            {'Franco': 'Person'},
            {'Madrid': 'Location'}
        ]
        self.assertEqual(ents, expected_result)

    def test_ner_client_replace_all_symbols(self):
        model = NerClient()
        sent = 'Franco lives% in Madrid.'
        sent_cleansed = model.sent_cleaning(sent)
        expected_result = "Franco lives in Madrid"
        self.assertEqual(sent_cleansed, expected_result)

    def test_ner_client_fetch_entity_dict_list_from_model_given_known_multiple_entity_sent(self):
        model = NerClient()
        sent = 'Franco lives in Madrid.'
        ents = model.get_ents(sent)
        expected_result = [
            {'Franco': 'Person'},
            {'Madrid': 'Location'}
        ]
        self.assertEqual(ents, expected_result)



