from os.path import join

from underthesea.file_utils import CACHE_ROOT

corpus_folder = join(CACHE_ROOT, "datasets", "VLSP2013-WTK-R2")
train = join(corpus_folder, "test.txt")
with open(train, "r") as f:
    sentences = f.read().split("\n\n")[:-1]
# sentences = sentences[:5000]

num_tokens_range = range(2, 15)
tree = {}
for num_tokens in num_tokens_range:
    tree_key = f"{num_tokens}gram"
    tree[tree_key] = {}


def index_nodes(num_tokens, i, n, nodes):
    global tree
    if i + num_tokens - 1 >= n:
        return
    tree_key = f"{num_tokens}gram"
    tree_node = tree[tree_key]
    phrase = " ".join([nodes[index][0] for index in range(i, i + num_tokens)])
    tag = " ".join([nodes[index][1] for index in range(i, i + num_tokens)])
    if phrase not in tree_node:
        tree_node[phrase] = {}
    if tag not in tree_node[phrase]:
        tree_node[phrase][tag] = 0
    tree_node[phrase][tag] += 1


for index, sentence in enumerate(sentences):
    if index % 5000 == 0:
        print(index)
    nodes = sentence.split("\n")
    nodes = [n.split("\t") for n in nodes if not n.startswith("#")]
    i = 0
    words = []
    n = len(nodes)
    while i < n:
        for num_tokens in num_tokens_range:
            index_nodes(num_tokens, i, n, nodes)
        i += 1


def analyze_ngram(num_tokens):
    global tree
    tree_key = f"{num_tokens}gram"
    print(tree_key, len(tree[tree_key]))
    count = 0
    count_conflict = 0
    for node in tree[tree_key]:
        if "B-W" + " I-W" * (num_tokens - 1) in tree[tree_key][node]:
            count += 1
            keys = list(tree[tree_key][node].keys())
            conflict_keys = [key for key in keys if key.startswith("B-W B-W")]
            if len(conflict_keys) > 0:
                print(node)
                print(tree[tree_key][node])
                count_conflict += 1
    print(f"{tree_key} word: {count}")
    print(f"{tree_key} conflict: {count_conflict}")
    print()


for i in num_tokens_range:
    analyze_ngram(i)
