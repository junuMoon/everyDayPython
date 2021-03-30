import re
import spacy


class NerClient:

    def __init__(self):
        self.ner_model = spacy.load("en_core_web_sm")
        self.model = {
            'Franco': 'Person',
            'Madrid': 'Location'
        }

    def get_ents_by_ner_model(self, sent):
        doc = self.ner_model(sent)
        return doc

    def get_ents(self, sent):
        sent = self.sent_cleaning(sent)
        words = sent.split(' ')
        ents = []
        for word in words:
            if word in self.model.keys():
                ents.append({word: self.model[word]})
        return ents

    @staticmethod
    def sent_cleaning(sent):
        sent = re.sub(r"[^a-zA-Z\s]", "", sent)
        return sent
