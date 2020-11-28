from export.data import VLSP2020_DP_R1, Corpus
from export.models.biaffine_dependency_parser import BiaffineDependencyParser
from wip_vlsp2020_dp.export.trainers import ParserTrainer

corpus: Corpus = VLSP2020_DP_R1()

embeddings = 'char'
embed = False
parser = BiaffineDependencyParser(embeddings, embed=False)
trainer = ParserTrainer(parser, corpus)
trainer.train(
    base_path='tmp/resources/parsers/dp',
    max_epochs=1,
    mu=0      # optimizer parameters
)
