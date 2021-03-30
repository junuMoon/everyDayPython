import spacy


class NerClient:

    def __init__(self):
        self.model = spacy.load("en_core_web_sm")
        self.label_map = {
            'PERSON': 'Person',
            'GPE': 'Location',
            'MONEY': 'Money',
            'ORG': 'Organization',
        }

    def get_ents(self, sent):
        doc = self.model(sent)
        ents = []
        for ent in doc.ents:
            ents.append({ent.text: self.label_map.get(ent.label_)})

        return ents
