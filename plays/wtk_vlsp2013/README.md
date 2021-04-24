# Build Vietnamese Word Segmentation using VLSP2013 corpus

* [Colab Notebook](https://colab.research.google.com/drive/1TooB3dyGWB86YkFjTKM4l8rkuTUCQDs2?usp=sharing)

## Download dataset 

``` 
export VLSP2013_WTK_URL=[]
underthesea download-data VLSP2013-WTK $VLSP2013_WTK_URL
underthesea revise -c VLSP2013-WTK
underthesea validate -t TOKENIZE -c VLSP2013-WTK-R2
```
