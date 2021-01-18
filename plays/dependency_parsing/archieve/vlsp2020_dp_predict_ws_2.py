import os
from os import listdir
from underthesea import word_tokenize
from underthesea.file_utils import DATASETS_FOLDER
import re

DP_FOLDER = f'{DATASETS_FOLDER}/VLSP2020-DP-V1A2'
TEST_FOLDER = f'{DP_FOLDER}/DataTestDP2020'
OUTPUT_FOLDER = f'{DP_FOLDER}/Output/System2.1'
os.system(f'rm -rf {OUTPUT_FOLDER}')
os.system(f'mkdir {OUTPUT_FOLDER}')


def normalize_forms(forms):
    output_forms = []
    for form in forms:
        if ('LBKT' in form or 'RBKT' in form) and (form != 'LBKT' and form != 'RBKT'):
            indices = []
            for match in re.finditer('LBKT|RBKT', form):
                start_pos, end_pos = match.span()
                indices.append(start_pos)
                indices.append(start_pos + 4)
            if indices[0] != 0:
                indices.insert(0, 0)
            if indices[-1] != len(form):
                indices.append(len(form))
            start_index = 0
            for i in range(1, len(indices)):
                output_forms.append(form[start_index:indices[i]].strip())
                start_index = indices[i]
        else:
            output_forms.append(form)
    return output_forms


def create_output_sentence(sentence):
    sentence = sentence.replace('LBKT', ' LBKT ')
    sentence = sentence.replace('RBKT', ' RBKT ')
    forms = word_tokenize(sentence)
    forms = normalize_forms(forms)
    lemmas = [form.lower() for form in forms]
    ids = [str(i + 1) for i in range(len(forms))]
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
