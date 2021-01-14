from pathlib import Path
import yaml
from underthesea.file_utils import CACHE_ROOT
from underthesea.word_tokenize import tokenize
#from underthesea.models.crf_sequence_tagger import CRFSequenceTagger
from external import CRFSequenceTagger


def load_model(base_path):
    with open(Path(base_path) / "model.metadata", "r") as f:
        metadata = yaml.safe_load(f)
    model_type = metadata["model"]
    if model_type == "CRFSequenceTagger":
        model = CRFSequenceTagger()
        model.load(base_path)
        return model
    return None


def word_tokenize(tagger, sentence):
    tokens = tokenize(sentence)
    tags = tagger.predict(tokens)
    output = []
    for tag, token in zip(tags, tokens):
        if tag == "I-W":
            output[-1] = output[-1] + u" " + token
        else:
            output.append(token)
    if format == "text":
        output = u" ".join([item.replace(" ", "_") for item in output])
    return output


if __name__ == '__main__':
    base_path = Path(CACHE_ROOT) / "models/wtk_crf_2"
    tagger = load_model(base_path)
    sentence = 'Chàng trai 9X Quảng Trị khởi nghiệp từ nấm sò'
    output = word_tokenize(tagger, sentence)
    print(output)
