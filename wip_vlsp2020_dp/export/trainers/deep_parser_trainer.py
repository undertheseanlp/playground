from os.path import join
from underthesea.file_utils import CACHE_ROOT
from wip_vlsp2020_dp.export.models.biaffine_dependency import BiaffineDependencyParser

class DeepParserTrainer:
    def __init__(self, parser, corpus):
        self.parser = parser
        self.corpus = corpus

    def train(self, max_epochs=10):
        DATASETS_FOLDER = join(CACHE_ROOT, 'datasets')
        CORPUS = join(DATASETS_FOLDER, 'VLSP2020-DP-R1')
        args = {
            'feat': 'char',
            'build': True,
            'train': f'{CORPUS}/train.txt',
            'test': f'{CORPUS}/test.txt',
            'dev': f'{CORPUS}/dev.txt',
            'embed': False
        }

        parser = BiaffineDependencyParser.build(path='tmp/dp', **args)
        parser.train(train=args['train'], dev=args['dev'], test=args['test'], epochs=max_epochs)
