import shutil
from os import makedirs

from vlsp2013_wtk.regex_tokenize import tokenize

stat_folder = "stats"
filename = "data/UNEWS-100K-V1.txt"

token_dictionary = {}
with open(filename) as f:
    for i, line in enumerate(f):
        tokens = tokenize(line)
        for token, token_type in tokens:
            if token_type not in token_dictionary:
                token_dictionary[token_type] = {}
            if token not in token_dictionary[token_type]:
                token_dictionary[token_type][token] = 0
            token_dictionary[token_type][token] += 1
        if i % 1000 == 0:
            print(i)
        # if i > 1000:
        #     break

print(token_dictionary)

shutil.rmtree(stat_folder)
makedirs(stat_folder)
for token_type in token_dictionary:
    values = token_dictionary[token_type]
    print(token_type, ":", len(values.items()))
    with open(f"{stat_folder}/{token_type}.txt", "w") as f:
        for token, freq in values.items():
            f.write(f"{token},{freq}\n")

