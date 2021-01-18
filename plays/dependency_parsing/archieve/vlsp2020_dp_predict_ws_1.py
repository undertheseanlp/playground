import os
from os import listdir
from underthesea import word_tokenize
from underthesea.file_utils import DATASETS_FOLDER

DP_FOLDER = f'{DATASETS_FOLDER}/VLSP2020-DP-V1A2'
TEST_FOLDER = f'{DP_FOLDER}/DataTestDP2020'
OUTPUT_FOLDER = f'{DP_FOLDER}/OutputSystem1'
os.system(f'rm -rf {OUTPUT_FOLDER}')
os.system(f'mkdir {OUTPUT_FOLDER}')


def create_output_sentence(sentence):
    sentence = sentence.replace('LBKT', 'LBKT ')
    sentence = sentence.replace('RBKT', ' RBKT')
    forms = word_tokenize(sentence)
    lemmas = [form.lower() for form in forms]
    ids = [str(i+1) for i in range(len(forms))]
    nodes = [node for node in zip(ids, forms, lemmas)]
    nodes = ['\t'.join(node) for node in nodes]
    output = '\n'.join(nodes)
    return output


def create_output(input_file, output_file):
    content = open(input_file).read()
    sentences = content.strip().split('\n')
    sentences = [s for s in sentences if s != '']
    sentences = [create_output_sentence(s) for s in sentences]
    output_content = '\n\n'.join(sentences)
    with open(output_file, 'w') as f:
        f.write(output_content)


for input_file in listdir(TEST_FOLDER):
    output_file = input_file[:-4] + '_output.txt'
    print(f'Process {input_file}')
    input_file = f'{TEST_FOLDER}/{input_file}'
    output_file = f'{OUTPUT_FOLDER}/{output_file}'
    create_output(input_file, output_file)
