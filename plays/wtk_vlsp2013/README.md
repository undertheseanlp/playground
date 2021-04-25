# Build Vietnamese Word Segmentation using VLSP2013 corpus

* [Colab Notebook](https://colab.research.google.com/drive/1TooB3dyGWB86YkFjTKM4l8rkuTUCQDs2?usp=sharing)

## Download dataset 

``` 
export VLSP2013_WTK_URL=[]
underthesea download-data VLSP2013-WTK $VLSP2013_WTK_URL
underthesea revise -c VLSP2013-WTK
underthesea validate -t TOKENIZE -c VLSP2013-WTK-R2
```

## Benchmarking

**VLSP 2013**

The training set consists of 75k manually word-segmented sentences (about 23 words per sentence in average). The test set consists of 2120 sentences (about 31 words per sentence) in 10 files from 800001.seg to 800010.seg.

<table>
  <tr>
    <th>Model</th>
    <th>F1</th>
    <th>Method</th>
    <th>Reference</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>Underthesea v1.3.2-alpha.1</td>
    <td>97</td>
    <td>Conditional Random Fields</td>
    <td></td>
    <td></td>
  </tr>
</table>