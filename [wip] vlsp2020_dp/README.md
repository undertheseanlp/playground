# Dependence Parsing

Tập dữ liệu [VLSP2020 DP](https://vlsp.org.vn/vlsp2020/eval/udp)

* train: gộp 2 file 
* test: 400

```
export MALT_PARSER=/home/anhv/Downloads/maltparser-1.9.2
python train_malt.py

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

