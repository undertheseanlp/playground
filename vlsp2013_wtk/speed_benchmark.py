import logging
import time
from os.path import join
from pathlib import Path

from pyvi import ViTokenizer
from underthesea.file_utils import DATASETS_FOLDER, CACHE_ROOT

from vlsp2013_wtk.predict import load_model, word_tokenize

logging.root.setLevel(logging.NOTSET)
FORMAT = '%(asctime)-11s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('playground')

file = join(DATASETS_FOLDER, "LTA", "VNESEScorpus.txt")


# Pyvi
f = open(file, "r")
start = time.time()
for i, line in enumerate(f):
    ViTokenizer.tokenize(line)
    if i % 10000 == 0:
        logger.info(i)
    if i == 100000:
        break
end = time.time()
print("Pyvi", end - start)
f.close()

base_path = Path(CACHE_ROOT) / "models/wtk_crf_2"
tagger = load_model(base_path)

# Predict
f = open(file, "r")
start = time.time()
for i, line in enumerate(f):
    output = word_tokenize(tagger, line)
    if i % 10000 == 0:
        logger.info(i)
    if i == 100000:
        break
end = time.time()
print("Underthesea", end - start)
f.close()