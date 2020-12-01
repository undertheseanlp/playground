import os
from os.path import dirname, isdir

from underthesea.file_utils import CACHE_ROOT


REVISE_VERSION = 1
os.system(f'rm -rf {CACHE_ROOT}/datasets/VLSP2020-DP-R{REVISE_VERSION}')
os.system(f'cp -r {CACHE_ROOT}/datasets/VLSP2020-DP-O {CACHE_ROOT}/datasets/VLSP2020-DP-R{REVISE_VERSION}')

O_FOLDER = f'{CACHE_ROOT}/datasets/VLSP2020-DP-O'
R_FOLDER = f'{CACHE_ROOT}/datasets/VLSP2020-DP-R{REVISE_VERSION}'

# merge VTB_2996 and DP-Package2.18.11.2020 -> train.txt
src_1_file = open(f'{O_FOLDER}/DP-Package2.18.11.2020.txt', 'r')
src_2_file = open(f'{O_FOLDER}/VTB_2996.txt', 'r')
dst_file = open(f'{R_FOLDER}/train.txt', 'w')
c1 = src_1_file.read()
c2 = src_2_file.read()
dst_file.write(c1)
dst_file.write(c2)

src_1_file.close()
src_2_file.close()
dst_file.close()

# revise vtb_400 -> test.txt
origin_file = open(f'{O_FOLDER}/VTB_400.txt', 'r')
r1_file = open(f'{R_FOLDER}/test.txt', 'w')

for i, line in enumerate(origin_file):
    line_number = i + 1
    if line_number == 4373:
        line = '5\tđể\tđể\tADP\tPre\t-\t7\tmark:pcomp\t-\t-\n'
    r1_file.write(line)

origin_file.close()
r1_file.close()

# copy test.txt -> dev.txt
os.system(f'cp {R_FOLDER}/test.txt {R_FOLDER}/dev.txt')

# split test -> dev, test
# sample train
DATASET_VERSION = 'v1.0.0-a0'
S_FOLDER = f'{CACHE_ROOT}/datasets/VLSP2020-DP-R1'
D_FOLDER = f'{CACHE_ROOT}/datasets/VLSP2020-DP-{DATASET_VERSION}'
os.system(f'rm -rf {D_FOLDER}')
os.system(f'mkdir {D_FOLDER}')

def read_sentences(file):
    sentences = open(file).read().split('\n\n')
    return sentences

def save_sentences(file, sentences):
    content = '\n\n'.join(sentences)
    with open(file, 'w') as f:
        f.write(content)

# train: sample 50 sentences
s_file = f'{S_FOLDER}/train.txt'
d_file = f'{D_FOLDER}/train.txt'
sentences = read_sentences(s_file)
sentences = sentences[:10]
save_sentences(d_file, sentences)

# dev: 50 sentences from test
s_file = f'{S_FOLDER}/test.txt'
d_dev_file = f'{D_FOLDER}/dev.txt'
d_test_file = f'{D_FOLDER}/test.txt'
sentences = read_sentences(s_file)
dev_sentences = sentences[:50]
test_sentences = sentences[50:100]
save_sentences(d_dev_file, dev_sentences)
save_sentences(d_test_file, test_sentences)
