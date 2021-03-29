import spacy


# need higher level of instruction
class NamedEntityClient:
    def __init__(self, model):
        self.model = model
        pass

    def get_ents(self, sent):
        doc = self.model(sent)
        entities = [{'ent': ent.text, 'label': self.map_label(ent.label_)} for ent in doc.ents]
        return {'ents': entities, 'html': ""}

    @staticmethod
    def map_label(label):
        label_map = {
            'PERSON': 'Person',
            'NORP': 'Group',
            'LOC': 'Location',
            'GPE': 'Location',
            'LANGUAGE': 'Language'
        }

        return label_map.get(label)