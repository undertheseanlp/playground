# [WIP] A simple experiment with Vietnamese Dependence Parsing

`wip`, `help-wanted`, `vietnamese-dependence-parsing`, `date:nov-2020`

```
Author     : Vu Anh
Last Update: Nov 2020 
```

### Introduction

Dependency parsing is the task of extracting a dependency parse of a sentence that represents its grammatical structure 
and defines the relationships between "head" words and words, which modify those heads. 

In this experiments, we try to build our very first dependency parser using VLSP2020 Dependence Parsing dataset and MatlParser, some deep learning methods [WIP]. We also wonder how Vietnamese word embeddings (e.g. PhoBert) works on dependency parsing task [TBD].

There are some deep learning methods for dependence parser tasks, begin with Manning work (2016), we focus on *biaffine attention* [[1]](#references) - a proven method which give a best result in VLSP 2019.

### Background and Related Work

These are several studies about Vietnamese Dependency Parsing

* In 2008, N.L. Minh et al: MST parser on a corpus consisting of 450 sentences.
* In 2013, N.T. Luong et al: MatlParser on a Vietnamese dependency treebank
* In 2014, N. Q. Dat et al: a new conversion method to automatically transform a constiuent-based VietTreebank in to dependency trees
* In 2017, N. K. Hieu: build BKTreebank, a dependency treebank for Vietnamese
* In 2017, a Vietnamese dependency treebank of 3,000 sentences is included for the CoNLL shared-task: "Multilingual Parsing from Raw Text to Universal Dependencies": 48 dependency labels for Vietnamese based on Stanford dependency labels set.
* In 2019, Vietnamese dependency parsing shared task in VLSP2019
* In 2020, VLSP organized the second shared task about dependency parsing

### Experiments Description

In these experiments, we use MaltParser as a baseline method. We further do some experiments with deep learning methods, especially *biaffine attention* [[1]](#references) method.

**MaltParser**

MaltParser is developed by Johan Hall, Jens Nilsson and Joankim Nivre. It is a data-driven parser generator for dependency parsing. Giving a treebank in dependency format, MaltParser can be used to induce a parser for the language of the treebank. MaltParser supports several parsing algorithms and learning algorithms, and allows user-defined models, consisting of arbitrary combinations of lexical features, part-of-speech features and dependency features. 

We run a simple MaltParser experiment with default config (see table 1)

Table 1: Default configs for MaltParser

```
2planar
  reduceonswitch (-2pr)                 false
config
  logfile (-lfi)                        stdout
  workingdir (  -w)                     user.dir
  name (  -c)                           dp-model-2
  logging ( -cl)                        info
  flowchart (  -m)                      learn
  type (  -t)                           singlemalt
  url (  -u)                            
covington
  allow_shift ( -cs)                    false
  allow_root ( -cr)                     true
graph
  max_sentence_length (-gsl)            256
  root_label (-grl)                     ROOT
  head_rules (-ghr)                     
guide
  features (  -F)                       
  data_split_threshold (  -T)           50
  kbest_type ( -kt)                     rank
  data_split_structure (  -s)           
  data_split_column (  -d)              
  learner (  -l)                        liblinear
  decision_settings (-gds)              T.TRANS+A.DEPREL
  classitem_separator (-gcs)            ~
  kbest (  -k)                          -1
input
  charset ( -ic)                        UTF-8
  reader ( -ir)                         tab
  reader_options (-iro)                 
  format ( -if)                         /appdata/dataformat/conllx.xml
  infile (  -i)                         /home/anhv/.underthesea/datasets/VLSP2020-DP-R1/train.txt
  iterations ( -it)                     1
lib
  external ( -lx)                       
  save_instance_files ( -li)            false
  options ( -lo)                        
  verbosity ( -lv)                      silent
multiplanar
  planar_root_handling (-prh)           normal
nivre
  enforce_tree ( -nt)                   true
  allow_reduce ( -ne)                   false
  allow_root ( -nr)                     true
output
  charset ( -oc)                        UTF-8
  outfile (  -o)                        
  format ( -of)                         
  writer_options (-owo)                 
  writer ( -ow)                         tab
planar
  no_covered_roots (-pcov)               false
  acyclicity (-pacy)                     true
  connectedness (-pcon)                  none
pproj
  marking_strategy ( -pp)               none
  lifting_order (-plo)                  shortest
  covered_root (-pcr)                   none
singlemalt
  mode ( -sm)                           parse
  diagnostics ( -di)                    false
  use_partial_tree ( -up)               false
  propagation ( -fp)                    
  parsing_algorithm (  -a)              nivreeager
  guide_model ( -gm)                    single
  null_value ( -nv)                     one
  diafile (-dif)                        stdout 
```

**Explore Deep Learning model**

We try to make [supar code](https://github.com/yzhangcs/parser) work on Vietnamese Dependency Parsing task.

### Dataset

**VLSP2020 Dependency Parsing Dataset**

We show test results on the [VLSP 2020 Dependency Parsing dataset](https://vlsp.org.vn/vlsp2020/eval/udp), training data 
consists 10,000 dependency-annotated sentences. We concat two file `DP-Package2.18.11.2020.txt` and `VTB_2996.txt` as 
training data, and get `VTB_400.txt` file as test data. 

### (current) Results

Detail score after using MaltParser, we consider this result as baseline of our experiments  

Table 2: detail score using MaltParser
 
```
Metric     | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
UFeats     |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     75.41 |     75.41 |     75.41 |     75.41
LAS        |     66.11 |     66.11 |     66.11 |     66.11
CLAS       |     62.70 |     62.17 |     62.43 |     62.17
MLAS       |     60.74 |     60.23 |     60.48 |     60.23
BLEX       |     62.70 |     62.17 |     62.43 |     62.17 
```

To reproduce this result, you can run 

```
export MALT_PARSER=/home/anhv/Downloads/maltparser-1.9.2
python train_malt.py 
```

### References

[1] Dozat, T., & Manning, C. D. (2017). Deep biaffine attention for neural dependency parsing. ArXiv:1611.01734 [Cs]. http://arxiv.org/abs/1611.01734