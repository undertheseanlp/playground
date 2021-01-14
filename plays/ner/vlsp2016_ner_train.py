from os.path import join

import torchtext
from underthesea.file_utils import DATASETS_FOLDER

data_folder = join(DATASETS_FOLDER, "VLSP2016-NER")

# corpus = torchtext.datasets.SequenceTaggingDataset(data_folder, fields=fields)
# print(0)