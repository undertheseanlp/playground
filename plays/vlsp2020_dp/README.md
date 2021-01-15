# Tutorial: Training a Vietnamese Dependency Parser

This part of the tutorial shows how you can train your own Vietnamese Dependency Parser using VLSP2020 Dependency Parsing dataset.

### Training a model

```
python vlsp2020_dp_train.py 
```

Result

```
Metric     | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     99.34 |     99.34 |     99.34 |     99.34
XPOS       |     99.34 |     99.34 |     99.34 |     99.34
UFeats     |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     99.34 |     99.34 |     99.34 |     99.34
Lemmas     |     99.93 |     99.93 |     99.93 |     99.93
UAS        |     81.53 |     81.53 |     81.53 |     81.53
LAS        |     72.96 |     72.96 |     72.96 |     72.96
CLAS       |     68.94 |     68.65 |     68.79 |     68.65
MLAS       |     66.76 |     66.49 |     66.62 |     66.49
BLEX       |     68.87 |     68.59 |     68.73 |     68.59 
```
