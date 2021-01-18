from os import listdir

from underthesea.file_utils import DATASETS_FOLDER

VLSP2020_DP = f'{DATASETS_FOLDER}/VLSP2020-DP-O'
files = listdir(VLSP2020_DP)
files = [file for file in files if file not in ['MotaDulieuDot1.txt', 'DataTestDP2020']]

texts = []


def parse_sentence(s):
    global texts
    nodes = s.split('\n')
    nodes = [n.split('\t') for n in nodes]

    text = " ".join([n[1] for n in nodes])
    texts.append(text)
    return text, nodes


def read_sentences(file):
    sentences = open(file).read().strip().split('\n\n')
    sentences = [parse_sentence(s) for s in sentences]
    return sentences


datasets = {}
print('\n\n+ ANALYZE TRAIN DATASET\n\n')
for file in files:
    sentences = read_sentences(f'{VLSP2020_DP}/{file}')
    datasets[file] = sentences
    n = len(sentences)
    print(f'{file}: {n}')

keys = sorted(list(datasets))

for k in keys:
    s = [i[0] for i in datasets[k]]
    unique_s = set(s)
    n_total = len(s)
    n_uniq = len(unique_s)
    n_dup = n_total - n_uniq
    print(f'\n{k}')
    print(f'Total: {n_total}')
    print(f'Unique: {n_uniq}')
    print(f'Duplicate: {n_dup}')

for i in range(len(keys)):
    si = [_[0] for _ in datasets[keys[i]]]
    unique_si = set(si)
    for j in range(i + 1, len(keys)):
            print(f'\n{keys[i]} - {keys[j]}')
            sj = [_[0] for _ in datasets[keys[j]]]
            unique_sj = set(sj)
            s_inter = unique_si.intersection(unique_sj)
            print(f'Intersections: {len(s_inter)}')
            # if len(s_inter) > 0:
            #     print(f'Samples:')
            #     print('\n'.join(list(s_inter)[:3]))

print('\n\n+ ANALYZE TEST DATASET\n\n')
