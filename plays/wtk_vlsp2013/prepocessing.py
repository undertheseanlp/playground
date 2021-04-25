from os import listdir
from os.path import join
from underthesea import word_tokenize

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
        return sentences


def create_craft_corpus():
    corpus_folder = 'tmp/CP_Vietnamese-UNC'
    sentences = TextCorpus.load(corpus_folder)
    train_file = join('tmp', 'corpus', 'train.txt')
    with open(train_file, 'w') as f:
        f.write('')
    f = open(train_file, 'a')
    for s in sentences:
        tokens = word_tokenize(s)
        for token in tokens:
            syllables = token.split(" ")
            # write first syllable
            syllable = syllables[0]
            f.write(f'{syllable}\tB-W\n')
            # write other syllable
            for syllable in syllables[1:]:
                f.write(f'{syllable}\tI-W\n')
        f.write('\n')
    f.close()
    print('Done')



if __name__ == '__main__':
    # download CP_Vietnamese-UNC corpus
    # url https://github.com/undertheseanlp/resources/releases/download/1.3.x/CP_Vietnamese-UNC.zip
    create_craft_corpus()
