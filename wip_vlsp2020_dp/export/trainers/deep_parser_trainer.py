from pathlib import Path
from typing import Union

from export.models.biaffine_dependency_parser import BiaffineDependencyParserSupar


class DeepParserTrainer:
    def __init__(self, parser, corpus):
        self.parser = parser
        self.corpus = corpus

    def train(self, base_path: Union[Path, str], max_epochs=10):
        r"""
        Train any class that implement model interface

        Args:
            base_path (object): Main path to which all output during training is logged and models are saved

        """
        args = {
            'feat': 'char',
            'build': True,
            'train': self.corpus.train,
            'test': self.corpus.test,
            'dev': self.corpus.dev,
            'embed': False
        }
        parser_supar = BiaffineDependencyParserSupar.build(path='tmp/dp', **args)
        parser_supar.train(train=self.corpus.train, dev=self.corpus.dev, test=self.corpus.test, epochs=max_epochs)
