from export.data import DPTagger, VLSP2020_DP_R1
from wip_vlsp2020_dp.export.trainers.mp_trainer import MaltParserTrainer

tagger = DPTagger(name='dp-model-2')
corpus = VLSP2020_DP_R1()
trainer = MaltParserTrainer(tagger, corpus)

trainer.train()
