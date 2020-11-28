from export.data import VLSP2020_DP_R1, Corpus
from export.models.biaffine_dependency_parser import BiaffineDependencyParser
from wip_vlsp2020_dp.export.trainers.deep_parser_trainer import DeepParserTrainer

corpus: Corpus = VLSP2020_DP_R1()

embeddings = 'char'
embed = False
parser = BiaffineDependencyParser(embeddings, embed=False)
trainer = DeepParserTrainer(parser, corpus)
trainer.train(base_path='tmp/resources/parsers/dp',
              max_epochs=10)
