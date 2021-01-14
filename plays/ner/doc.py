class Document:
    def __init__(self):
        pass


class Sentence:
    def __init__(self, tokens):
        self._tokens = tokens
        self._words = []
        self._dependences = []
        self._text = None
        self._ents = []
