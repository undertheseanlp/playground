from export.data import VLSP2020_DP_R1, Corpus
from export.models.biaffine_dependency_parser import BiaffineDependencyParserSupar, BiaffineDependencyParser
from wip_vlsp2020_dp.export.trainers.deep_parser_trainer import DeepParserTrainer

corpus: Corpus = VLSP2020_DP_R1()

parser = BiaffineDependencyParser()
trainer = DeepParserTrainer(parser, corpus)
trainer.train(base_path='tmp/dp',
              max_epochs=2)
