from underthesea.models.dependency_parser import BiaffineDependencyParser
from underthesea.trainers.parser_trainer import ParserTrainer

from export.data import VLSP2020_DP_R1, Corpus


corpus: Corpus = VLSP2020_DP_R1()

embeddings = 'char'
embed = False
parser = BiaffineDependencyParser(embeddings, embed=False)
trainer = ParserTrainer(parser, corpus)
trainer.train(
    base_path='tmp/resources/parsers/dp',
    max_epochs=1000,
    mu=0      # optimizer parameters
)
