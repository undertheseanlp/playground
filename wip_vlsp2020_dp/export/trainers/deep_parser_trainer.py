import logging
import os
from supar.utils.field import Field, SubwordField
from pathlib import Path
from typing import Union
from supar.utils.common import bos, pad, unk
from supar.utils.transform import CoNLL

from export import device
from export.models.biaffine_dependency_parser import BiaffineDependencyParserSupar
from supar.utils import Config, Dataset, Embedding

from export.modules.model import BiaffineDependencyModel
from export.utils.logging import get_logger, init_logger

logger = get_logger(__name__)
init_logger(logger)


class DeepParserTrainer:
    def __init__(self, parser, corpus):
        self.parser = parser
        self.corpus = corpus

    def train(self, base_path: Union[Path, str],
              fix_len=20,
              min_freq=2,
              max_epochs=10):
        r"""
        Train any class that implement model interface

        Args:
            max_epochs:
            min_freq:
            fix_len:
            base_path (object): Main path to which all output during training is logged and models are saved

        """
        ################################################################################################################
        # BUILD
        ################################################################################################################
        locals_args = {
            'base_path': base_path,
            'fix_len': fix_len,
            'min_freq': min_freq,
            'max_epochs': max_epochs
        }
        args = Config(**locals_args)
        args.feat = self.parser.embeddings
        args.embed = self.parser.embed
        os.makedirs(os.path.dirname(base_path), exist_ok=True)

        logger.info("Building the fields")
        WORD = Field('words', pad=pad, unk=unk, bos=bos, lower=True)
        if args.feat == 'char':
            FEAT = SubwordField('chars', pad=pad, unk=unk, bos=bos, fix_len=args.fix_len)
        elif args.feat == 'bert':
            from transformers import AutoTokenizer
            tokenizer = AutoTokenizer.from_pretrained(args.bert)
            args.max_len = min(args.max_len or tokenizer.max_len, tokenizer.max_len)
            FEAT = SubwordField('bert',
                                pad=tokenizer.pad_token,
                                unk=tokenizer.unk_token,
                                bos=tokenizer.bos_token or tokenizer.cls_token,
                                fix_len=args.fix_len,
                                tokenize=tokenizer.tokenize)
            FEAT.vocab = tokenizer.get_vocab()
        else:
            FEAT = Field('tags', bos=bos)

        ARC = Field('arcs', bos=bos, use_vocab=False, fn=CoNLL.get_arcs)
        REL = Field('rels', bos=bos)
        if args.feat in ('char', 'bert'):
            transform = CoNLL(FORM=(WORD, FEAT), HEAD=ARC, DEPREL=REL)
        else:
            transform = CoNLL(FORM=WORD, CPOS=FEAT, HEAD=ARC, DEPREL=REL)

        train = Dataset(transform, self.corpus.train)
        WORD.build(train, min_freq, (Embedding.load(args.embed, unk) if self.parser.embed else None))
        FEAT.build(train)
        REL.build(train)
        args.update({
            'n_words': WORD.vocab.n_init,
            'n_feats': len(FEAT.vocab),
            'n_rels': len(REL.vocab),
            'pad_index': WORD.pad_index,
            'unk_index': WORD.unk_index,
            'bos_index': WORD.bos_index,
            'feat_pad_index': FEAT.pad_index,
            'device': device,
            'path': base_path
        })
        model = BiaffineDependencyModel(**args)
        model.load_pretrained(WORD.embed).to(device)
        parser_supar = BiaffineDependencyParserSupar(args, model, transform)

        ################################################################################################################
        # TRAIN
        ################################################################################################################
        parser_supar.train(train=self.corpus.train,
                           dev=self.corpus.dev,
                           test=self.corpus.test,
                           epochs=max_epochs,
                           verbose=True)
