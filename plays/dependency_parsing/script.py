from os import listdir
from os.path import join, basename
import os

path = '/home/anhv/Downloads/DataTestGoldDP2020'


def load_file(file):
    text = open(file).read().strip()
    sentences = text.split('\n\n')
    return sentences


files = [file for file in listdir(path)]
files = [join(path, file) for file in files if file.endswith(".txt")]
[load_file(file) for file in files]


# create system 1
def evaluate(system_folder):
    output_file = 'system_output.txt'
    sentences = load_file(join(path, system_folder, 'Test-from-vtb_output.conllu'))
    sentences = sentences[:906]
    files = [
        'test-vnexpress-1_output.conllu',
        'test-vnexpress-3_output.conllu',
        'test-vnexpress-7_output.conllu',
        'test-vnexpress-8_output.conllu',
        'test-vnexpress-10_output.conllu',
        'test-vnexpress-14_output.conllu'
    ]
    content = '\n\n'.join(sentences) + '\n\n'
    for file in files:
        sentences = load_file(join(path, system_folder, file))
        content += '\n\n'.join(sentences) + '\n\n'
    with open(join(path, output_file), 'w') as f:
        f.write(content)

    print(system_folder)
    os.chdir(path)
    os.system(f'python conll18_ud_eval.py -v total-gold.txt {output_file}')
    print('\n\n')


evaluate('System1')
evaluate('System2')
evaluate('System3')
evaluate('System4')
