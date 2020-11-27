from os.path import join

import torch
from supar import BiaffineDependencyParser
from supar.utils import CoNLL
from underthesea.file_utils import CACHE_ROOT

from wip_vlsp2020_dp.export.modules.model import BiaffineDependencyModel

# model = BiaffineDependencyModel(10, 10, 5)
#
# words = torch.tensor([[1, 2, 3, 4, 5]])
# feats = torch.tensor([[[2], [3], [1], [4], [5]]])
#
# output = model(words, feats)
# print(output)

# args = type("Args", (object, ), {})()
# args.feat = 'char'
# args.build = False

DATASETS_FOLDER = join(CACHE_ROOT, 'datasets')
CORPUS = join(DATASETS_FOLDER, 'VLSP2020-DP-R1')
args = {
    'feat': 'char',
    'build': False,
    'train': f'{CORPUS}/train.txt',
    'test': f'{CORPUS}/test.txt',
    'dev': f'{CORPUS}/dev.txt',
    'embed': False
}
model = BiaffineDependencyModel(10, 10, 10)
transform = CoNLL()
parser = BiaffineDependencyParser.build(path='tmp/dp', **args)

parser.train(train=args['train'], dev=args['dev'], test=args['test'])
