from os import listdir
from os.path import join


class TextCorpus:
    @staticmethod
    def load(corpus_folder):
        files = listdir(corpus_folder)
        files = [join(corpus_folder, file) for file in files]
        sentences = []
        for file in files:
            with open(file) as f:
                _ = f.read().splitlines()
                _ = [item for item in _ if not item.startswith("#")]
                sentences.extend(_)
        print(0)


def create_craft_corpus():
    corpus_folder = 'tmp/CP_Vietnamese-UNC'
    TextCorpus.load(corpus_folder)


if __name__ == '__main__':
    # download CP_Vietnamese-UNC corpus
    # url https://github.com/undertheseanlp/resources/releases/download/1.3.x/CP_Vietnamese-UNC.zip
    create_craft_corpus()
