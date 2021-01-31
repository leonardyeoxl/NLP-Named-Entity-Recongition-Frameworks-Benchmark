import stanza
from decorators import *

@timer
def predict(nlp):
    doc = nlp("When I told John that I wanted to move to Alaska, he warned me that I'd have trouble finding a Starbucks there.")

if __name__ == "__main__":
    stanza.download('en')       # This downloads the English models for the neural pipeline
    nlp = stanza.Pipeline('en') # This sets up a default neural pipeline in English
    predict(nlp)