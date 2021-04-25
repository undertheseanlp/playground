import hydra
from omegaconf import DictConfig
import logging

log = logging.getLogger(__name__)

def f1():
    log.info("hihi")

@hydra.main(config_path="configs/", config_name="config.yaml")
def main(config: DictConfig):
    print(config)
    f1()


if __name__ == "__main__":
    main()