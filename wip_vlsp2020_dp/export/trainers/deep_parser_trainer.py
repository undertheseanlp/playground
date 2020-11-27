from pathlib import Path
from typing import Union


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
        self.parser.train(train=self.corpus.train, dev=self.corpus.dev, test=self.corpus.test, epochs=max_epochs)
