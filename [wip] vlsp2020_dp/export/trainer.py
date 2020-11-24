import os
from underthesea.file_utils import DATASETS_FOLDER, CACHE_ROOT
from types import SimpleNamespace

from conll18_ud_eval import evaluate_wrapper, evaluate_wrapper2
from export.data import DPTagger


class DPTrainer:
    def __init__(self, tagger: DPTagger, corpus):
        self.tagger = tagger
        self.corpus = corpus

    def train(self):
        print("Train Dependency Parsing")
        assert 'MALT_PARSER' in os.environ, 'You must set MALT_PARSER environment variable before running this script'

        MALT_PARSER = os.environ['MALT_PARSER']

        model_name = self.tagger.name

        train_file = self.corpus.train
        train_cmd = f'java -jar {MALT_PARSER}/maltparser-1.9.2.jar -nt true -c {model_name} -i {train_file} -m learn'
        print(train_cmd)
        os.system(train_cmd)

        test_file = self.corpus.test
        system_file = 'tmp_output.conll'
        test_cmd = f'java -jar {MALT_PARSER}/maltparser-1.9.2.jar -c {model_name} -i {test_file} -o {system_file} -nt true -m parse'
        print(test_cmd)
        os.system(test_cmd)

        args = SimpleNamespace()
        args.gold_file = self.corpus.test
        args.system_file = system_file
        args.verbose = False
        args.counts = False
        evaluate_wrapper2(args)
