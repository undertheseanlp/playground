from export.data import DPTagger, VLSP2020_DP_R1
from export.trainer import DPTrainer


tagger = DPTagger(name='dp-model-2')
corpus = VLSP2020_DP_R1()
trainer = DPTrainer(tagger, corpus)

trainer.train()
