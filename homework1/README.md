# README

## 题目

用sklearn实现聚类算法

## 要求

分别在 `digits` 和 `20newsgroups` 两个数据集上做以下聚类算法：

- K-Means
- Affinity propagation
- Mean-shift
- Spectral clustering
- Agglomerative clustering
- DBSCAN
- Gaussian mixtures

并按照以下评估标准进行评估：

- Normalized Mutual Information(NMI)
  - `metrics.normalized_mutual_info_score(labels_true, labels_pred)`
- Homogeneity: each cluster contains only members of a single class
  - `metrics.homogeneity_score(labels_true, labels_pred)`
- Completeness: all members of a given class are assigned to the same cluster
  - `metrics.completeness_score(labels_true, labels_pred)`

## 环境

Jupyter Notebook

## 内容

### 1 数据集

使用的数据集有 Digits（手写数字）数据集和 20newsgroups（文章）数据集。

Digits 数据集是用矩阵形式存储的单通道图像，可视化后如下图：

![img](data:image/png;base64,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)

20newsgroups 数据集是纯文本形式的数据集。

## 运行结果

[图形化的运行结果点这里](https://nbviewer.jupyter.org/github/rayiooo/python_datamining_rayiooo/blob/master/homework1/main.ipynb)

### 1 Digits聚类运行结果

```
                    	NMI		Homo	Comp
k-means             	0.690	0.670	0.712
AffinityPropagation 	0.616	0.932	0.460
MeanShift           	0.660	0.833	0.546
SpectralClustering  	0.828	0.805	0.853
AgglomerativeClustering	0.796	0.758	0.836
DBSCAN              	0.621	0.887	0.477
GaussianMixture     	0.679	0.657	0.702
```

### 2 20NewsGroup聚类运行结果

```
						NMI		Homo	Comp
k-means             	0.440	0.439	0.442
AffinityPropagation 	0.289	0.921	0.172
MeanShift           	0.271	0.909	0.159
SpectralClustering  	0.480	0.444	0.522
AgglomerativeClustering	0.473	0.454	0.492
DBSCAN              	0.273	0.919	0.161
GaussianMixture     	0.427	0.427	0.427
--------------------------------------------------
```


## 结论

- SpectralClustering、AgglomerativeClustering 效果最好。
- AffinityPropagation、MeanShift、DBSCAN 效果最差。
- k-means、GaussianMixture 表现还不错。