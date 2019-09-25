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

## 运行结果

[图形化的运行结果点这里](https://nbviewer.jupyter.org/github/rayiooo/python_datamining_rayiooo/blob/master/homework1/main.ipynb)

### 1 Digits聚类运行结果

```
                    	NMI	Homo	Comp
k-means             	0.690	0.670	0.712
AffinityPropagation 	0.669	0.665	0.674
MeanShift           	0.470	1.000	0.307
SpectralClustering  	0.828	0.805	0.853
AgglomerativeClustering	0.796	0.758	0.836
DBSCAN              	0.613	0.605	0.621
GaussianMixture     	0.680	0.654	0.709
```

### 2 20NewsGroup聚类运行结果

```
                    	NMI	Homo	Comp
k-means             	0.441	0.440	0.443
AffinityPropagation 	0.289	1.000	0.169
MeanShift           	0.269	0.901	0.158
SpectralClustering  	0.481	0.444	0.523
AgglomerativeClustering	0.473	0.454	0.494
DBSCAN              	0.428	0.437	0.419
GaussianMixture     	0.439	0.438	0.440
```


## 结论

表现最好的是 SpectralClustering 和 AgglomerativeClustering 聚类算法，它们在两个数据集上都达到了很好的效果。

K-Means 和 GaussianMixture 聚类算法表现不错，并且比较稳定。

AffinityPropagation、MeanShift、DBSCAN 算法对参数的依赖性非常强，调参得当得到的结果也不差，但是调参十分困难，很难找到能够得到较好结果的参数。

AffinityPropagation 耗时最久，因为其时间复杂度很高。MeanShift也比较慢，但参数`bin_seeding=True`可以大大加快它的运行速度。

## 各聚类算法优缺点

### K-Means

优点：

* 算法简单。
* 复杂度较低。

缺点：

* 随机初始化的中心点对结果影响很大。

### AffinityPropagation

AP算法的基本思想是将全部样本看作网络的节点，然后通过网络中各条边的消息传递计算出各样本的聚类中心。

在实际计算应用中，最重要的两个参数（也是需要手动指定）是Preference和Damping factor。前者定了聚类数量的多少，值越大聚类数量越多；后者控制算法收敛效果。

优点：

* 无需指定聚类数量。
* 样本质心是某个数据点，而不是一些数据点的平均。
* 不要求矩阵对称性。
* 对初始值选择不敏感。

缺点：

* 时间复杂度较高（`O(N*N*logN)`），计算需要很久。
* 计算效果非常依赖Preference和Damping两个参数。

### Mean-shift

Mean-shift算法是一个迭代的步骤，即先算出当前点的偏移均值，将该点移动到此偏移均值，然后以此为新的起始点，继续移动，直到满足最终的条件。

Mean-shift算法在本实验中表现不好。

### Spectral clustering

谱聚类的主要思想是把所有的数据看做空间中的点，这些点之间可以用边连接起来。距离较远的两个点之间的边权重值较低，而距离较近的两个点之间的边权重值较高，通过对所有数据点组成的图进行切图，让切图后不同的子图间边权重和尽可能的低，而子图内的边权重和尽可能的高，从而达到聚类的目的。

优点：

* 谱聚类只需要数据之间的相似度矩阵，因此对于处理稀疏数据的聚类很有效。这点传统聚类算法比如K-Means很难做到。
* 由于使用了降维，因此在处理高维数据聚类时的复杂度比传统聚类算法好。

缺点：

* 如果最终聚类的维度非常高，则由于降维的幅度不够，谱聚类的运行速度和最后的聚类效果均不好。
* 聚类效果依赖于相似矩阵，不同的相似矩阵得到的最终聚类效果可能很不同。

### Agglomerative clustering

Agglomerative Clutsering 是一种自底而上的层次聚类方法，它能够根据指定的相似度或距离定义计算出类之间的距离。

优点：

- 无需指定聚类数量。
- 对于距离度量标准的选择并不敏感。


缺点：

* 时间复杂度高（`O(n³)`）。

### DBSCAN

DBSCAN是一种基于密度的聚类算法，它类似于均值漂移，但具有一些显著的优点。

优点：

* 无需指定聚类数量。
* 能够识别噪声。
* 能发现任意形状的聚类。

缺点：

* cluster密度不同时表现不好。
* 非常依赖参数epsilon和minPoints。
* 在高维度表现不好。（因此在该实验中表现不好）

### Gaussian mixtures

高斯混合模型（GMMs）比 K-Means更有灵活性。每个簇的形状都可以用均值和标准差来描述，因此这些簇可以采取任何类型的椭圆形。

优点：

* 应用最为广泛。
* 收敛速度快。
* 能扩展以用于大规模的数据集。

缺点：

* 倾向于识别凸形分布、大小相近、密度相近的聚类。
* 中心选择和噪声聚类对结果影响大。

