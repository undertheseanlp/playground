from os import listdir
import pandas as pd
from underthesea.file_utils import DATASETS_FOLDER

TEST_FOLDER = f'{DATASETS_FOLDER}/VLSP2020-DP-V1A2/DataTestDP2020'
files = sorted(listdir(TEST_FOLDER))

stats = {}
data = []


def analyze_file(file):
    global stats
    global data
    count_less_20 = 0
    count_20_40 = 0
    count_40_80 = 0
    count_80_100 = 0
    count_more_100 = 0
    content = open(f'{TEST_FOLDER}/{file}').read()
    sentences = content.strip().split('\n')
    sentences = [s for s in sentences if s != '']
    for s in sentences:
        n = len(s)
        if n < 20:
            count_less_20 += 1
        elif n < 40:
            count_20_40 += 1
        elif n < 80:
            count_40_80 += 1
        elif n < 100:
            count_80_100 += 1
        else:
            count_more_100 += 1
    num_sentences = len(sentences)
    print(file)
    print('# sentences:', num_sentences)
    print()
    data.append((file, num_sentences, count_less_20, count_20_40, count_40_80, count_80_100, count_more_100))


for file in files:
    analyze_file(file)

df = pd.DataFrame(data, columns=['file_id', 'total', '<20', '20_40', '40_80', '80_100', '100+'])
print(df)
df.to_csv('output.csv')

