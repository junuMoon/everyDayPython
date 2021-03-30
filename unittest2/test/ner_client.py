import re


class NerClient:

    def __init__(self):
        self.model = {
            'Franco': 'Person',
            'Madrid': 'Location'
        }

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
