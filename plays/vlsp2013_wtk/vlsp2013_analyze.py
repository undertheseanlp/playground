import sys
from pathlib import Path

from underthesea.feature_engineering.text import Text
from underthesea.word_tokenize.regex_tokenize import tokenize
import difflib

DATA_FOLDER = "/home/anhv/.underthesea/datasets/VLSP2013-WTK"

count = 0
cases = []


incorrect = [
    4707, 5343, 5589, 6250, 9366, 11046, 11047, 11048, 11049, 11050, 11053, 11066, 11082,
    11067, 13469, 13471, 13774, 20644, 26348, 24367, 21801, 29379, 29195, 24366, 32869, 36783, 39838, 35791, 42251,
    40555, 43492, 43493, 46762, 47015, 49117, 49454, 49455, 49456, 49457, 49458, 49475, 51144,
    56004, 56005, 56007, 57675, 57730, 60000, 57731, 60191, 60193, 60194, 60409, 61258, 61891, 62695, 64192, 64364, 64365,
    67254, 67975, 68201, 68307, 68488, 68560, 68591, 68827, 68828, 68829, 68849, 68851, 68854, 68928, 69030, 69801,
    69803, 69810,
    69813, 69887, 69891, 69901, 69945, 70141, 70319, 70396, 70397, 70403, 70423, 70425, 70719, 71087, 71357, 71493,
    72006, 72649, 72721, 72768, 72781, 72720, 73071, 73376, 73543, 73693, 73732, 73562,
    73807, 73821, 73829, 73830, 73832, 73840, 73869, 74256, 74263, 74252, 74264, 74266, 74269, 74270, 74271, 74291,
    74294, 74295, 74300, 74311, 74313, 74362, 75053, 75364,
    73730, 73731, 73724, 73718, 73720, 73709, 73397,
]

laters = set([
    # name (e.g. Th.T., Lê Th.Ng.)
    6106, 7050,
    6784, 11471,
    12531, 12532, 20820, 23973, 29548, 29539, 29107,
    49920, 49948, 63009, 63517, 67226, 68642, 68644, 68695, 68726,
    # dấu chấm
    69656, 71276, 74188, 75280, 75345, 75344, 75354, 75346,
    # nhóm máu (e.g. Rh-)
    8198, 8201, 8206, 8212, 8219, 8220,
    # nhiệt độ
    68699,  68700,
    # ký hiệu
    70242, 70487,
    # number
    # 27546, 26954,
    # email (e.g. krongpac@)
    12196, 46547, 46552, 46556, 46562, 46573, 67225,
    # etc
    73573,
    # others
    3014, 3813, 3860, 4687, 4688, 8546,
    14511, 24424, 26317, 32586, 39404, 40346, 41071,
    14912,  # B.52
    43328, 52468, 54347, 57839, 59155, 59159, 67782, 68919, 70090, 70165, 70499, 70553, 70617, 70627,
    72379, 72380, 72428, 72861, 72880, 72427, 72885, 75286, 75289, 26954, 27546
])


def extract_text(i, s):
    if i in incorrect or i in laters:
        return
    global count
    global cases
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
        cases.append(i)
    if count > 30:
        print(cases)
        sys.exit(1)


with open(Path(DATA_FOLDER) / "train.txt") as f:
    sentences = f.read().strip().split("\n\n")
    [extract_text(i, s) for i, s in enumerate(sentences)]
print(cases)
