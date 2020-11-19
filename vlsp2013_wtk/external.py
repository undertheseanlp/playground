from os.path import join
from pathlib import Path
import joblib
import pycrfsuite
import re
from underthesea.transformer.tagged_feature import functions


# code from
# underthesea.transformer.tagged import TaggedTransformer
class TaggedTransformer:
    def __init__(self, templates=None):
        self.templates = [self._extract_template(template) for template in templates]

    def _extract_template(self, template):
        token_syntax = template
        matched = re.match(
            "T\[(?P<index1>\-?\d+)(\,(?P<index2>\-?\d+))?\](\[(?P<column>.*)\])?(\.(?P<function>.*))?",
            template)
        column = matched.group("column")
        column = int(column) if column else 0
        index1 = int(matched.group("index1"))
        index2 = matched.group("index2")
        index2 = int(index2) if index2 else None
        func = matched.group("function")
        return index1, index2, column, func, token_syntax

    def word2features(self, s):
        features = []
        for i, token in enumerate(s):
            tmp = []
            for template in self.templates:
                index1, index2, column, func, token_syntax = template
                prefix = "%s=" % token_syntax

                if i + index1 < 0:
                    result = "%sBOS" % prefix
                    tmp.append(result)
                    continue
                if i + index1 >= len(s):
                    result = "%sEOS" % prefix
                    tmp.append(result)
                    continue
                if index2 is not None:
                    if i + index2 >= len(s):
                        result = "%sEOS" % prefix
                        tmp.append(result)
                        continue
                    tokens = [s[j][column] for j in range(i + index1, i + index2 + 1)]
                    word = " ".join(tokens)
                else:
                    try:
                        word = s[i + index1][column]
                    except Exception:
                        pass
                if func is not None:
                    result = functions[func](word)
                else:
                    result = word
                result = "%s%s" % (prefix, result)
                tmp.append(result)
            features.append(tmp)
        return features

    def transform(self, sentences, contain_labels=False):
        X = [self.word2features(sentence) for sentence in sentences]
        if contain_labels:
            y = [self.sentence2labels(s) for s in sentences]
            return X, y
        return X

    def sentence2labels(self, s):
        return [row[-1] for row in s]


# code from
# from underthesea.models.crf_sequence_tagger import CRFSequenceTagger
class CRFSequenceTagger:
    def __init__(self, features=None):
        self.features = features
        self.estimator = None
        self.transformer = None

    def forward(self, samples, contains_labels=False):
        if not self.transformer:
            self.transformer = TaggedTransformer(self.features)
        return self.transformer.transform(samples, contains_labels)

    def save(self, path):
        joblib.dump(self.features, path)

    def load(self, base_path):
        model_path = str(Path(base_path) / "model.bin")
        estimator = pycrfsuite.Tagger()
        estimator.open(model_path)
        features = joblib.load(join(base_path, "features.bin"))
        transformer = TaggedTransformer(features)
        self.transformer = transformer
        self.estimator = estimator

    def predict(self, tokens):
        tokens = [(token, ) for token in tokens]
        x = self.transformer.transform([tokens])[0]
        tags = self.estimator.tag(x)
        return tags
