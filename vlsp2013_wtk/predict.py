from pathlib import Path
import yaml
from underthesea.file_utils import CACHE_ROOT


# underthesea.models.crf_sequence_tagger
class CRFSequenceTagger:
    def __init__(self):
        pass

    def load(self, base_path):
        print(base_path)


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


base_path = Path(CACHE_ROOT) / "models/wtk_crf_2"
model = load_model(base_path)
print(model)
