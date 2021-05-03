import hydra
from omegaconf import DictConfig
from underthesea.datasets.data import DataReader
from underthesea.models.crf_sequence_tagger import CRFSequenceTagger
from underthesea.trainers import ModelTrainer
import logging

log = logging.getLogger(__name__)


@hydra.main(config_path="configs/", config_name="config.yaml")
def main(config: DictConfig):
    def load_feature_from_hydra_config(hydra_config_features):
        features = [_.split("::") for _ in hydra_config_features]
        features = [_ for sublist in features for _ in sublist]
        return features

    features = load_feature_from_hydra_config(config.model.features)
    tagger = CRFSequenceTagger(features)
    data_folder = config.dataset.data_folder
    train_file = config.dataset.train_file
    test_file = config.dataset.test_file

    log.info('Dataset:')
    log.info(config.dataset)
    log.info('Model:')
    log.info(config.model)
    log.info('Trainer:')
    log.info(config.trainer)
    log.info('base_path:')
    log.info(config.base_path)

    corpus = DataReader.load_tagged_corpus(data_folder, train_file=train_file, test_file=test_file)
    corpus = corpus.downsample(config.dataset.downsample)
    trainer = ModelTrainer(tagger, corpus)

    params = {
        'c1': config.model.c1,  # coefficient for L1 penalty
        'c2': config.model.c2,  # coefficient for L2 penalty
        'max_iterations': config.trainer.max_iterations,  #
        # include transitions that are possible, but not observed
        'feature.possible_transitions': True,
        'feature.possible_states': True,
    }

    trainer.train(config.base_path, params)


if __name__ == "__main__":
    main()
