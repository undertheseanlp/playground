import os
import shutil
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from underthesea.corpus.categorized_corpus import CategorizedCorpus
from underthesea.data_fetcher import DataFetcher, NLPData
from underthesea.models.text_classifier import TextClassifier, TEXT_CLASSIFIER_ESTIMATOR
from underthesea.trainers.classifier_trainer import ClassifierTrainer

model_folder = "tmp/classification_svm_vntc"
try:
    shutil.rmtree(model_folder)
except:
    pass
finally:
    os.makedirs(model_folder)

tfidf__ngram_range = (1, 2)
tfidf__max_df = 0.5

start = time.time()
print(">>> Train VNTC Classification")
corpus: CategorizedCorpus = DataFetcher.load_corpus(NLPData.VNTC)
print("\n\n>>> Sample sentences")
for s in corpus.train[:10]:
    print(s)
pipeline = Pipeline(
    steps=[
        ('features', TfidfVectorizer(ngram_range=tfidf__ngram_range, max_df=tfidf__max_df)),
        ('estimator', LinearSVC())
    ]
)
print("\n\n>>> Start training")
classifier = TextClassifier(estimator=TEXT_CLASSIFIER_ESTIMATOR.PIPELINE, pipeline=pipeline)
model_trainer = ClassifierTrainer(classifier, corpus)


def micro_f1_score(y_true, y_pred):
    return f1_score(y_true, y_pred, average='micro')


model_trainer.train(model_folder, scoring=micro_f1_score)
print(f"\n\n>>> Finish training in {round(time.time() - start, 2)} seconds")
print(f"Your model is saved in {model_folder}")
