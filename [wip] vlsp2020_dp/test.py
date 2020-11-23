import os

from underthesea.file_utils import DATASETS_FOLDER, CACHE_ROOT

assert 'MALT_PARSER' in os.environ, 'You must set MALT_PARSER environment variable before running this script'

MALT_PARSER = os.environ['MALT_PARSER']

model_name = 'dp-model'

VLSP2020_DP_FOLDER = f'{DATASETS_FOLDER}/VLSP2020-DP-R1'


test_file = f'{VLSP2020_DP_FOLDER}/VTB_400.txt'
test_cmd = f'java -jar {MALT_PARSER}/maltparser-1.9.2.jar -c {model_name} -i {test_file} -o out.conll -m parse'
print(test_cmd)
os.system(test_cmd)
