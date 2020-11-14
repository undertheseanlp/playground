from pathlib import Path
import yaml
from underthesea.file_utils import CACHE_ROOT
from underthesea.models.crf_sequence_tagger import CRFSequenceTagger
from underthesea.word_tokenize import tokenize


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
    global wtk_model
    tokens = tokenize(sentence)
    tags = wtk_model.predict(tokens)
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
    wtk_model = load_model(base_path)
    sentence = 'Chàng trai 9X Quảng Trị khởi nghiệp từ nấm sò'
    output = word_tokenize(sentence)
    print(output)
