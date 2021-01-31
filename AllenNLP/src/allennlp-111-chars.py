from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging
from decorators import *

@timer
def predict(predictor):
    prediction = predictor.predict(
        sentence="When I told John that I wanted to move to Alaska, he warned me that I'd have trouble finding a Starbucks there."
    )
    # print(prediction)

if __name__ == "__main__":
    predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/ner-model-2020.02.10.tar.gz")
    predict(predictor)