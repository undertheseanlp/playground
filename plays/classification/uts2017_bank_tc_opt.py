import os
import time
from os import listdir

from hyperopt import hp, Trials, fmin, tpe
from languageflow.data import CategorizedCorpus
from languageflow.data_fetcher import NLPData, DataFetcher
from languageflow.models.text_classifier import TextClassifier, TEXT_CLASSIFIER_ESTIMATOR
from languageflow.trainers.model_trainer import ModelTrainer
from sacred import Experiment
from sacred.observers import MongoObserver
from sacred.optional import np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.svm import SVC

from text_features import Lowercase, RemoveTone, CountEmoticons

ex = Experiment('bank_31')
ex.observers.append(MongoObserver.create())


@ex.main
def my_run(estimator__C,
           features__lower_pipe__tfidf__max_features,
           features__lower_pipe__tfidf__ngram_range,
           features__with_tone_char__ngram_range,
           features__remove_tone__tfidf__ngram_range):
    params = locals().copy()
    start = time.time()
    print(params)
    corpus: CategorizedCorpus = DataFetcher.load_corpus(NLPData.UTS2017_BANK_TC)
    pipeline = Pipeline(
        steps=[
            ('features', FeatureUnion([
                ('lower_pipe', Pipeline([
                    ('lower', Lowercase()),
                    ('tfidf', TfidfVectorizer(norm='l2', min_df=2))])),
                ('with_tone_char', TfidfVectorizer(norm='l2', min_df=2, analyzer='char')),
                ('remove_tone', Pipeline([
                    ('remove_tone', RemoveTone()),
                    ('lower', Lowercase()),
                    ('tfidf', TfidfVectorizer(norm='l2', min_df=2))])),
                ('emoticons', CountEmoticons())
            ])),
            ('estimator', SVC(kernel='linear', class_weight=None, verbose=True))
        ]
    )
    pipeline.set_params(**params)
    classifier = TextClassifier(estimator=TEXT_CLASSIFIER_ESTIMATOR.PIPELINE, pipeline=pipeline)
    model_trainer = ModelTrainer(classifier, corpus)
    tmp_model_folder = "tmp/tmp_model"

    def micro_f1_score(y_true, y_pred):
        return f1_score(y_true, y_pred, average='micro')

    score = model_trainer.train(tmp_model_folder, scoring=micro_f1_score)
    tmp_files = listdir(tmp_model_folder)
    for file in tmp_files:
        if "gitignore" in file:
            continue
        os.remove(f"{tmp_model_folder}/{file}")
    ex.log_scalar('dev_score', score['dev_score'])
    ex.log_scalar('test_score', score['test_score'])
    print(f"Time: {round(time.time() - start, 2)} s")
    return score['dev_score']


best_score = 1.0


def objective(space):
    global best_score
    test_score = ex.run(config_updates=space).result
    score = 1 - test_score
    print("Score:", score)
    return score


space = {
    'estimator__C': hp.choice('estimator__C', np.arange(0.01, 0.9, 0.01)),
    'features__lower_pipe__tfidf__max_features': hp.choice('features__lower_pipe__tfidf__max_features',
                                                           np.arange(1000, 10000, 1000)),
    'features__lower_pipe__tfidf__ngram_range': hp.choice('features__lower_pipe__lower_tfidf__ngram_range',
                                                          [(1, 3), (1, 4), (1, 5), (1, 6)]),
    'features__with_tone_char__ngram_range': hp.choice('features__with_tone_char__ngram_range',
                                                       [(1, 3), (1, 4), (1, 5), (1, 6)]),
    'features__remove_tone__tfidf__ngram_range': hp.choice('features__remove_tone__tfidf__ngram_range',
                                                           [(1, 3), (1, 4), (1, 5), (1, 6)])
}

start = time.time()
trials = Trials()
best = fmin(objective, space=space, algo=tpe.suggest, max_evals=500, trials=trials)

print(f"Hyperopt search took {round(time.time() - start, 2)} seconds for 500 candidates")
print(-best_score, best)
