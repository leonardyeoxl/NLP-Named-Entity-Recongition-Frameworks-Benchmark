import spacy
from decorators import *

@timer
def predict(nlp):
    doc = nlp("When I told John that I wanted to move to Alaska, he warned me that I'd have trouble finding a Starbucks there.")
    # print([(w.text, w.pos_) for w in doc])

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    predict(nlp)