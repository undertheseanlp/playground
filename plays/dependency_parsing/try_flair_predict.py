from flair.data import Corpus, Sentence
# load the model you trained
from flair.models import SequenceTagger

model = SequenceTagger.load('tmp/resources/taggers/example-pos/final-model.pt')

# create example sentence
sentence = Sentence('I love Berlin')

# predict tags and print
model.predict(sentence)

print(sentence.to_tagged_string())
