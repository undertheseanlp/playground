from wip_vlsp2020_dp.export.trainers.deep_parser_trainer import DeepParserTrainer

parser = None
corpus = None
trainer = DeepParserTrainer(parser, corpus)
trainer.train(max_epochs=5)
