from typing import List

from flair.data import Sentence, Token
from flair.models import SequenceTagger

upos_model = SequenceTagger.load('tmp/taggers/upos/best-model.pt')

text_tokens_map = {}


def predict(tokens):
    global text_tokens_map
    global upos_model
    text = ' '.join(tokens)
    text_tokens_map[text] = tokens

    def custom_tokenizer(text: str) -> List[Token]:
        global text_tokens_map
        tokens = text_tokens_map[text]
        tokens: List[Token] = [Token(token) for token in tokens]
        return tokens

    sentence = Sentence(text, use_tokenizer=custom_tokenizer)
    upos_model.predict(sentence)
    tags = [token.labels[0].value for token in sentence]
    return tags

text = ['Lượng', 'heo', 'thịt', 'này', 'tôi', 'xuất', 'mỗi', 'đợt', 'hơn', '20.000', 'con']
tags = predict(text)

print(tags)
