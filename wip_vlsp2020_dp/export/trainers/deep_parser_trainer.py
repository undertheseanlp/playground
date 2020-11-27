class DeepParserTrainer:
    def __init__(self, parser, corpus):
        self.parser = parser
        self.corpus = corpus

    def train(self, max_epochs=10):
        r"""
        Train any class that implement model interface

        :param max_epochs:
        :return:
        """
        self.parser.train(train=self.corpus.train, dev=self.corpus.dev, test=self.corpus.test, epochs=max_epochs)
