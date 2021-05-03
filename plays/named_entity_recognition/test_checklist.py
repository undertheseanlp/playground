import checklist
from checklist.editor import Editor
from checklist.perturb import Perturb
from checklist.test_types import MFT, INV, DIR

editor = Editor()

# First, let's find some positive and negative adjectives
', '.join(editor.suggest('This is not {a:mask} {thing}.', thing=['book', 'movie', 'show', 'game'])[:30])

pos = ['good', 'enjoyable', 'exciting', 'excellent', 'amazing', 'great', 'engaging']
neg = ['bad', 'terrible', 'awful', 'horrible']

ret = editor.template('This is not {a:pos} {mask}.', pos=pos, labels=0, save=True, nsamples=100)
ret += editor.template('This is not {a:neg} {mask}.', neg=neg, labels=1, save=True, nsamples=100)

test = MFT(ret.data, labels=ret.labels, name='Simple negation',
           capability='Negation', description='Very simple negations.')

test = MFT(**ret, name='Simple negation',
           capability='Negation', description='Very simple negations.')

from pattern.en import sentiment

import numpy as np


def predict_proba(inputs):
    p1 = np.array([(sentiment(x)[0] + 1) / 2. for x in inputs]).reshape(-1, 1)
    p0 = 1 - p1
    return np.hstack((p0, p1))


predict_proba(['good', 'bad'])

from checklist.pred_wrapper import PredictorWrapper

wrapped_pp = PredictorWrapper.wrap_softmax(predict_proba)

wrapped_pp(['good'])

test.run(wrapped_pp)

test.summary()

test.visual_summary()
