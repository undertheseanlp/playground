import os
import shutil
import time
from os.path import join
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from underthesea.corpus.categorized_corpus import CategorizedCorpus
from underthesea.data_fetcher import DataFetcher, NLPData
from underthesea.file_utils import DATASETS_FOLDER
from underthesea.models.text_classifier import TextClassifier, TEXT_CLASSIFIER_ESTIMATOR
from underthesea.trainers.classifier_trainer import ClassifierTrainer

model_folder = "tmp/sa_svm_vlsp2016-sa_20210107"
shutil.rmtree(model_folder, ignore_errors=True)
os.makedirs(model_folder)

start = time.time()
print(">>> Train VLSP2016 SA Classification")
data_folder = Path(join(DATASETS_FOLDER, "VLSP2016-SA"))
corpus: CategorizedCorpus = DataFetcher.load_classification_corpus(data_folder)
print(corpus)
print("\n\n>>> Sample sentences")
for s in corpus.train[:10]:
    print(s)

pipeline = Pipeline(
    steps=[
        ('features', TfidfVectorizer(
            ngram_range=(1, 2),
            max_df=0.8)
         ),
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
