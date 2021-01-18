import os
from os import listdir
from underthesea import word_tokenize
from underthesea.file_utils import DATASETS_FOLDER
from typing import List
from flair.data import Sentence, Token
from flair.models import SequenceTagger

WS_FOLDER = f'{DATASETS_FOLDER}/VLSP2020-DP-V1A2/Output/System1.1'
POS_FOLDER = f'{DATASETS_FOLDER}/VLSP2020-DP-V1A2/Output/System1.2'
os.system(f'rm -rf {POS_FOLDER}')
os.system(f'mkdir {POS_FOLDER}')

pos_model = SequenceTagger.load('tmp/taggers/upos/best-model.pt')

text_tokens_map = {}


def upos_predict(tokens):
    global text_tokens_map
    global pos_model
    text = ' '.join(tokens)
    text_tokens_map[text] = tokens

    def custom_tokenizer(text: str) -> List[Token]:
        global text_tokens_map
        tokens = text_tokens_map[text]
        tokens: List[Token] = [Token(token) for token in tokens]
        return tokens

    sentence = Sentence(text, use_tokenizer=custom_tokenizer)
    pos_model.predict(sentence)
    tags = [token.labels[0].value for token in sentence]
    return tags


def create_output_sentence(sentence):
    nodes = sentence.split('\n')
    ids = [node.split('\t')[0] for node in nodes]
    forms = [node.split('\t')[1] for node in nodes]
    lemmas = [node.split('\t')[2] for node in nodes]
    upos_tags = upos_predict(forms)
    nodes = list(zip(ids, forms, lemmas, upos_tags))
    nodes = ['\t'.join(node) for node in nodes]
    sentence = '\n'.join(nodes)
    return sentence


def create_output(input_file, output_file):
    content = open(input_file).read()
    sentences = content.strip().split('\n\n')
    sentences = [create_output_sentence(s) for s in sentences]
    output_content = '\n\n'.join(sentences)
    with open(output_file, 'w') as f:
        f.write(output_content)


for file in listdir(WS_FOLDER):
    print(f'Process {file}')
    input_file = f'{WS_FOLDER}/{file}'
    output_file = f'{POS_FOLDER}/{file}'
    create_output(input_file, output_file)
