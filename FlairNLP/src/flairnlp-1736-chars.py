from flair.data import Sentence
from flair.models import SequenceTagger
from decorators import *

@timer
def predict(tagger):
    sentence = Sentence("Hong Kong, Seoul, Korea – January 20, 2021 – BASF has signed a global, exclusive supply agreement with Caregen, for four cosmetic peptides. With this expansion in its portfolio, BASF plans to launch four peptides with anti-aging and anti-pigmentation properties, for prone-atopic and prone-acneic skins, in the course of 2021.“There is robust growth in the dermocosmetics sector globally and especially in Asia, as more consumers desire targeted functionality from cosmetics, in line with the personalization trend. By using cosmetic products formulated with these peptides as active ingredients, consumers can have a choice of products with proven efficacy,” said Jeff Huh, Head of Marketing Personal Care Solutions at BASF Asia Pacific.“Peptides are widely used as biological actives in different markets. Selecting the most promising peptides from Caregen’s huge portfolio and adapting them to the standards of the cosmetic industry has been a great achievement of our team,” said David Hérault, Head of Global Product Development Bio-actives at BASF Care Chemicals.“Building on Caregen’s functional peptides with high technical and commercial competitiveness and BASF’s expertise in solutions and ingredients which are offered to the global cosmetics market, this agreement has both companies well set up for a long-term cooperation. With the ongoing functional health food and pharmaceutical product development, Caregen aims to soon become a leading peptide platform company, recognized by global customers,” said Dr. Chung Yong-Ji, CEO, Caregen. Caregen’s highly potent synthetic peptides will be a complementary technology to the bioactives and other cosmetic solutions and ingredients offered by BASF’s personal care portfolio.")

    # predict NER tags
    tagger.predict(sentence)

    # print sentence with predicted tags
    # print(sentence.to_tagged_string())

if __name__ == "__main__":
    tagger = SequenceTagger.load('ner')
    predict(tagger)