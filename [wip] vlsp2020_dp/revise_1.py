import os
from underthesea.file_utils import CACHE_ROOT

REVISE_VERSION = 1
os.system(f'rm -rf {CACHE_ROOT}/datasets/VLSP2020-DP-R{REVISE_VERSION}')
os.system(f'cp -r {CACHE_ROOT}/datasets/VLSP2020-DP-O {CACHE_ROOT}/datasets/VLSP2020-DP-R{REVISE_VERSION}')

O_FOLDER = f'{CACHE_ROOT}/datasets/VLSP2020-DP-O'
R1_FOLDER = f'{CACHE_ROOT}/datasets/VLSP2020-DP-R1'

# revise vtb_400
origin_file = open(f'{O_FOLDER}/VTB_400.txt', 'r')
r1_file = open(f'{R1_FOLDER}/VTB_400.txt', 'w')

for i, line in enumerate(origin_file):
    line_number = i + 1
    if line_number == 4373:
        line = '5\tđể\tđể\tADP\tPre\t-\t7\tmark:pcomp\t-\t-\n'
    r1_file.write(line)

origin_file.close()
r1_file.close()

