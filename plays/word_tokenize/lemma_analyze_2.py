import re
from os.path import join

from underthesea.file_utils import CACHE_ROOT

corpus_folder = join(CACHE_ROOT, "datasets", "VLSP2013-WTK-R2")
train = join(corpus_folder, "train.txt")
with open(train, "r") as f:
    sentences = f.read().split("\n\n")[:-1]

max_matched = 0


def extract_largest_word(sentence):
    global max_matched
    nodes = sentence.split("\n")
    nodes = [n.split("\t") for n in nodes if not n.startswith("#")]
    tags = " ".join([n[1] for n in nodes])
    matched = re.findall("(B-W(?: I-W)+)", tags)
    if matched:
        for m in matched:
            if len(m) > max_matched:
                print(m)
                print(len(m.split(" ")))
                print(nodes)
                max_matched = len(m)


for sentence in sentences:
    extract_largest_word(sentence)
