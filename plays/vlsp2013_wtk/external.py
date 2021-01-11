from os.path import join
from pathlib import Path
import joblib
import pycrfsuite
import re
from underthesea.transformer.tagged_feature import functions


# code from
# underthesea.transformer.tagged import TaggedTransformer
class FeatureTemplate:
    def __init__(self, template):
        token_syntax = template
        matched = re.match(
            "T\[(?P<index1>\-?\d+)(\,(?P<index2>\-?\d+))?\](\[(?P<column>.*)\])?(\.(?P<function>.*))?",
            template)
        column = matched.group("column")
        column = int(column) if column else 0
        index1 = int(matched.group("index1"))
        index2 = matched.group("index2")
        if index2:
            index2 = int(index2)
            assert index2 - index1 <= 2  # don't support ngram with n > 3
            if index2 - index1 == 1:
                self.is_bigram = True
            if index2 - index1 == 2:
                self.is_trigram = True
        func = matched.group("function")
        self.index1 = index1
        self.index2 = index2
        self.column = column
        self.func = func
        self.token_syntax = token_syntax


class TaggedTransformer:
    def __init__(self, templates=None):
        self.features = {
            "has_unigram": True,
            "has_bigram": False,
            "has_trigram": False,
            "bigram": {},
            "trigram": {}
        }
        self.raw_templates = templates
        self.templates = [self._extract_template(template) for template in templates]
        self.features_templates = [FeatureTemplate(template) for template in templates]

    def _extract_template(self, template):
        token_syntax = template
        matched = re.match(
            "T\[(?P<index1>\-?\d+)(\,(?P<index2>\-?\d+))?\](\[(?P<column>.*)\])?(\.(?P<function>.*))?",
            template)
        column = matched.group("column")
        column = int(column) if column else 0
        index1 = int(matched.group("index1"))
        index2 = matched.group("index2")
        if index2:
            index2 = int(index2)
            assert index2 - index1 <= 2  # don't support ngram with n > 3
            if index2 - index1 == 1:
                self.features["has_bigram"] = True
            if index2 - index1 == 2:
                self.features["has_trigram"] = True
        func = matched.group("function")
        return index1, index2, column, func, token_syntax

    def construct_values(self, nodes):
        values = {}
        self.values = values

    def nodes2features(self, nodes):
        features = []
        self.construct_values()
        for i, token in enumerate(nodes):
            tmp = []
            for template in self.templates:
                index1, index2, column, func, token_syntax = template
                prefix = "%s=" % token_syntax

                if i + index1 < 0:
                    result = "%sBOS" % prefix
                    tmp.append(result)
                    continue
                if i + index1 >= len(nodes):
                    result = "%sEOS" % prefix
                    tmp.append(result)
                    continue
                if index2 is not None:
                    if i + index2 >= len(nodes):
                        result = "%sEOS" % prefix
                        tmp.append(result)
                        continue
                    tokens = [nodes[j][column] for j in range(i + index1, i + index2 + 1)]
                    word = " ".join(tokens)
                else:
                    try:
                        word = nodes[i + index1][column]
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

    def transform(self, sentences):
        X = [self.nodes2features(sentence) for sentence in sentences]
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
        tokens = [(token,) for token in tokens]
        x = self.transformer.transform([tokens])[0]
        tags = self.estimator.tag(x)
        return tags
