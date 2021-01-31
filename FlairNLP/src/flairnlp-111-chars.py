from flair.data import Sentence
from flair.models import SequenceTagger
from decorators import *

@timer
def predict(tagger):
    sentence = Sentence("When I told John that I wanted to move to Alaska, he warned me that I'd have trouble finding a Starbucks there.")

    # predict NER tags
    tagger.predict(sentence)

    # print sentence with predicted tags
    # print(sentence.to_tagged_string())

if __name__ == "__main__":
    tagger = SequenceTagger.load('ner')
    predict(tagger)