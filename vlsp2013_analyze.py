import sys
from pathlib import Path

from underthesea.feature_engineering.text import Text
from underthesea.word_tokenize.regex_tokenize import tokenize
import difflib

DATA_FOLDER = "/home/anhv/.underthesea/datasets/VLSP2013-WTK"

count = 0
ignores = set([
    22,    # 78K-3274
    882,   # Ai-len
    883,   # Ai-len
    922,   # tung tr'ăy
    1055,  # - in middle
    1297,
    2055, 1047, 1053, 2645, 2687, 2789, 2811, 2815, 2789, 2908, 3014, 3529, 3551, 3752
])


def extract_text(i, s):
    if i in ignores:
        return
    global count
    s = Text(s)
    tokens_tags = [token.split("\t") for token in s.split("\n")]
    tokens = [token_tag[0] for token_tag in tokens_tags]
    text = " ".join(tokens)
    extract_tokens = tokenize(text)
    extract_text = " ".join(extract_tokens)

    if tokens != extract_tokens:
        count += 1
        print("==========")
        print(i)
        differ = difflib.Differ()
        diff = differ.compare([text], [extract_text])
        print("\n".join(diff))
    if count > 10:
        sys.exit(1)
    return text


with open(Path(DATA_FOLDER) / "train.txt") as f:
    sentences = f.read().strip().split("\n\n")
    [extract_text(i, s) for i, s in enumerate(sentences)]
