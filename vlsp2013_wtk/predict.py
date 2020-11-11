from pathlib import Path
import pycrfsuite
import yaml
from underthesea.file_utils import CACHE_ROOT
from underthesea.transformer.tagged import TaggedTransformer
from underthesea.word_tokenize import tokenize


class CRFSequenceTagger:
    def __init__(self, features=None, estimator=None):
        self.features = features
        self.estimator = None
        self.transformer = None

    def load(self, base_path):
        print(base_path)
        model_path = str(Path(base_path) / "model.tmp")
        estimator = pycrfsuite.Tagger()
        estimator.open(model_path)
        features = [
            # word unigram and bigram and trigram
            "T[-2]", "T[-1]", "T[0]", "T[1]", "T[2]",
            "T[-2,-1]", "T[-1,0]", "T[0,1]", "T[1,2]",
            "T[-2,0]", "T[-1,1]", "T[0,2]",

            "T[-2].lower", "T[-1].lower", "T[0].lower", "T[1].lower", "T[2].lower",
            "T[-2,-1].lower", "T[-1,0].lower", "T[0,1].lower", "T[1,2].lower",

            "T[-1].isdigit", "T[0].isdigit", "T[1].isdigit",

            "T[-2].istitle", "T[-1].istitle", "T[0].istitle", "T[1].istitle", "T[2].istitle",
            "T[0,1].istitle", "T[0,2].istitle",

            "T[-2].is_in_dict", "T[-1].is_in_dict", "T[0].is_in_dict", "T[1].is_in_dict", "T[2].is_in_dict",
            "T[-2,-1].is_in_dict", "T[-1,0].is_in_dict", "T[0,1].is_in_dict", "T[1,2].is_in_dict",
            "T[-2,0].is_in_dict", "T[-1,1].is_in_dict", "T[0,2].is_in_dict",
        ]
        transformer = TaggedTransformer(features)
        self.transformer = transformer
        self.estimator = estimator

    def predict(self, tokens):
        tokens = [(token, "X") for token in tokens]
        x = self.transformer.transform([tokens])[0]
        tags = self.estimator.tag(x)
        return tags


def load_model(base_path):
    with open(Path(base_path) / "model.metadata", "r") as f:
        metadata = yaml.safe_load(f)
    model_type = metadata["model"]
    print(model_type)
    if model_type == "CRFSequenceTagger":
        model = CRFSequenceTagger()
        model.load(base_path)
        return model
    return None


def word_tokenize(sentence):
    tokens = tokenize(sentence)
    tags = model.predict(tokens)
    output = []
    for tag, token in zip(tags, tokens):
        if tag == "I-W":
            output[-1] = output[-1] + u" " + token
        else:
            output.append(token)
    if format == "text":
        output = u" ".join([item.replace(" ", "_") for item in output])
    return output


base_path = Path(CACHE_ROOT) / "models/wtk_crf_2"
model = load_model(base_path)
sentence = 'Chàng trai 9X Quảng Trị khởi nghiệp từ nấm sò'
output = word_tokenize(sentence)
print(output)
