import logging
import time
from os.path import join
from pathlib import Path
from underthesea import sent_tokenize
from pyvi import ViTokenizer
from underthesea.file_utils import DATASETS_FOLDER, CACHE_ROOT

from predict import load_model, word_tokenize

logging.root.setLevel(logging.NOTSET)
FORMAT = '%(asctime)-11s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('playground')

file = join(DATASETS_FOLDER, "LTA", "VNESEScorpus.txt")

NUM_SENTS = 200
LOG_EVERY_NUM_SENTS = 50

# Predict
base_path = Path(CACHE_ROOT) / "models/wtk_crf_4"
tagger = load_model(base_path)
f = open(file, "r")
start = time.time()
for i, line in enumerate(f):
    output = word_tokenize(tagger, line)
    if i % LOG_EVERY_NUM_SENTS == 0:
        logger.info(i)
    if i == NUM_SENTS:
        break
end = time.time()
logger.info(f"Underthesea {end-start}")
f.close()

# Pyvi
f = open(file, "r")
start = time.time()
for i, line in enumerate(f):
    ViTokenizer.tokenize(line)
    if i % LOG_EVERY_NUM_SENTS == 0:
        logger.info(i)
    if i == NUM_SENTS:
        break
end = time.time()
logger.info(f"Pyvi {end-start}")
f.close()


