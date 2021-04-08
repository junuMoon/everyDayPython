class Sentence:
    def __init__(self, sent):
        self.sent = sent.split(' ').__iter__()
        
    def __iter__(self):  # make __iter__ dir
        return self
        
    def __next__(self):
        for word in self.sent:
            return word
        
class CoreySentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split(' ')
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]
    
class InfoSentence:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
        
    def __next__(self):
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration
        self._idx += 1
        return word
            
class InfoSentGenerator:
    def __init__(self, sent):
        self.sent = sent.split()
        
    def __iter__(self):
        for word in self.sent:
            yield word
        return

my_sentenc4 = InfoSentGenerator('This is a test')
my_sentenc4 = iter(my_sentenc4)
print(next(my_sentenc4))
print(next(my_sentenc4))
print(next(my_sentenc4))
    
my_sentence = Sentence('This is a test')
my_sentence2 = CoreySentence('This is a test')

def sentence(sentence):
    for word in sentence.split():
        yield word
        
my_sentence3 = sentence('Hi there from Korea')
    
