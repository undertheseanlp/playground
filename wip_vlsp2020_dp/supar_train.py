from export.data import VLSP2020_DP_R1, Corpus
from export.models.biaffine_dependency_parser import BiaffineDependencyParser
from wip_vlsp2020_dp.export.trainers.deep_parser_trainer import DeepParserTrainer

corpus: Corpus = VLSP2020_DP_R1()

args = {
    'feat': 'char',
    'build': True,
    'train': corpus.train,
    'test': corpus.test,
    'dev': corpus.dev,
    'embed': False
}
parser = BiaffineDependencyParser.build(path='tmp/dp', **args)
trainer = DeepParserTrainer(parser, corpus)
trainer.train(base_path='tmp/dp',
              max_epochs=2)
