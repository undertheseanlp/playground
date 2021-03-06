from os.path import join

from underthesea.datasets.vlsp2020_dp import VLSP2020_DP, VLSP2020_DP_SAMPLE
from underthesea.file_utils import MODELS_FOLDER
from underthesea.models.dependency_parser import DependencyParser
from underthesea.trainers.dependency_parser_trainer import DependencyParserTrainer

from src.models.embedings import FieldEmbeddings, CharacterEmbeddings

corpus = VLSP2020_DP()

embeddings = [
    FieldEmbeddings(),
    CharacterEmbeddings()
]
parser = DependencyParser(embeddings=embeddings, init_pre_train=True)
trainer: DependencyParserTrainer = DependencyParserTrainer(parser, corpus)
trainer.train(
    base_path=join(MODELS_FOLDER, 'parsers', 'vi-dp-v1.3.2a2'),
    max_epochs=1000,
    mu=.9  # optimizer parameters
)
