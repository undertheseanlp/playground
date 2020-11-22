import os

from underthesea.file_utils import DATASETS_FOLDER, CACHE_ROOT

assert 'MALT_PARSER' in os.environ, 'You must set MALT_PARSER environment variable before running this script'

MALT_PARSER = os.environ['MALT_PARSER']

model_name = 'dp-model'
MODELS_FOLDER = f'{CACHE_ROOT}/models/vlsp2020_dp'
model_file = f'{MODELS_FOLDER}/{model_name}'

VLSP2020_DP_FOLDER = f'{DATASETS_FOLDER}/VLSP2020-DP-O'
train_file = f'{VLSP2020_DP_FOLDER}/DP-Package2.18.11.2020.txt'
train_cmd = f'java -jar {MALT_PARSER}/maltparser-1.9.2.jar -c {model_name} -i {train_file} -m learn'
print(train_cmd)
os.system(train_cmd)

test_file = f'{VLSP2020_DP_FOLDER}/VTB_400.txt'
test_cmd = f'java -jar {MALT_PARSER}/maltparser-1.9.2.jar -c {model_name} -i {test_file} -o out.conll -m parse'
print(test_cmd)
os.system(test_cmd)
