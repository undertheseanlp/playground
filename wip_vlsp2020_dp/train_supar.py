from os.path import join
from supar import BiaffineDependencyParser
from supar.utils import CoNLL
from underthesea.file_utils import CACHE_ROOT
from playground.wip_vlsp2020_dp.export.modules.model import BiaffineDependencyModel

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
