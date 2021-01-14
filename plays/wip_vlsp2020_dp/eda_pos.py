from os import listdir
import pandas as pd
from underthesea.file_utils import DATASETS_FOLDER

DP_FOLDER = f'{DATASETS_FOLDER}/VLSP2020-DP-V1A2'
train_files = [
    'DP-Package2.18.11.2020.txt',
    'HTB_1570.txt',
    'SA-Hotel-50.txt',
    'SA-Restaurant-50.txt',
    'VTB_2996.txt',
    'VTB_400.txt'
]


def parse_sentence(s):
    nodes = s.split('\n')
    nodes = [n.split('\t') for n in nodes]
    return nodes


id_set = set()
form_set = set()
lemma_set = set()
upos_set = set()
upos_count = {}
xpos_set = set()
feats_set = set()
head_set = set()
deprel_set = set()
deps_set = set()
misc_set = set()
upos_xpos_map = {}
upos_deprel_map = {}


def analyze_sentence(s):
    global upos_xpos_map
    global id_set, form_set, lemma_set, upos_set, xpos_set, feats_set, head_set, deprel_set, deps_set, misc_set
    for node in s:
        id, form, lemma, upos, xpos, feats, head, deprel, deps, misc = node
        if upos not in upos_xpos_map:
            upos_xpos_map[upos] = set()
        if upos not in upos_deprel_map:
            upos_deprel_map[upos] = set()
        if upos not in upos_count:
            upos_count[upos] = 0
        upos_count[upos] += 1

        upos_xpos_map[upos].add(xpos)
        upos_deprel_map[upos].add(deprel)
        id_set.add(id)
        form_set.add(form)
        lemma_set.add(lemma)
        upos_set.add(upos)
        xpos_set.add(xpos)
        feats_set.add(feats)
        head_set.add(head)
        deprel_set.add(deprel)
        deps_set.add(deps)
        misc_set.add(misc)


for file in train_files:
    sentences = open(f'{DP_FOLDER}/{file}').read().strip().split('\n\n')
    sentences = [parse_sentence(s) for s in sentences]
    [analyze_sentence(s) for s in sentences]

print('=' * 20)
print(sorted(id_set))
print('=' * 20)
# print(sorted(form_set))
print(f'Unique forms: {len(form_set)}')
# print(sorted(lemma_set))
print(f'Unique lemmas: {len(lemma_set)}')
print('=' * 20)
print(sorted(upos_set))
print(f'Unique upox: {len(upos_set)}')
print('upos:\n', upos_count)
print(sorted(xpos_set))
print(f'Unique xpos: {len(xpos_set)}')
print('upos -> xpos')
print(upos_xpos_map)
print('=' * 20)
print(sorted(feats_set))
print('=' * 20)
print(sorted(head_set))
print('=' * 20)
print(sorted(deprel_set))
print(f'Unique deprel: {len(deprel_set)}')
print('upos -> deprel')
print(upos_deprel_map)
print('=' * 20)
print(sorted(deps_set))
print(sorted(misc_set))


def get_upos_id(name):
    id = name
    id = id.replace(':', '_')
    id = id.replace(' ', '_')
    return id


def get_xpos_id(name):
    id = name
    id = id.replace(':', '_')
    id = id.replace(' ', '_')
    id = 'X_' + id
    return id


def neo4j_export():
    global upos_xpos_map
    command = ''
    for upos in upos_set:
        upos_id = get_upos_id(upos)
        node_property = '{' + f"name: '{upos}'" + '}'
        command += f'CREATE ({upos_id}:UPOS {node_property})\n'

    for xpos in xpos_set:
        xpos_id = get_xpos_id(xpos)
        node_property = '{' + f"name: '{xpos}'" + '}'
        command += f'CREATE ({xpos_id}:XPOS {node_property})\n'

    for upos in upos_xpos_map:
        for xpos in upos_xpos_map:
            upos_id = get_upos_id(upos)
            xpos_id = get_xpos_id(xpos)
            command += f'CREATE ({upos_id})-[:e]->({xpos_id})\n'
    print('\n\nNeo4j Export')
    print(command)
    open('neo4j_command_export.txt', 'w').write(command)


neo4j_export()
