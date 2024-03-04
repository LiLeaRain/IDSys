# 基于PCA和滑动窗口的网络入侵检测系统设计与实现

## 收集数据集
需要一个包含网络流量数据的数据集，其中包括正常和异常的网络流量。
有几个地方可以找到开源数据集，适合用于网络入侵检测或其他机器学习任务：


### 本项目所用数据集
本项目以CICIDS 2017数据集为基础进行实现，数据集网站<https://www.unb.ca/cic/datasets/ids-2017.html>，使用该数据集需要引用
Iman Sharafaldin, Arash Habibi Lashkari, and Ali A. Ghorbani, "Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization", 4th International Conference on Information Systems Security and Privacy (ICISSP), Portugal, January 2018

这篇论文

## 数据预处理
对收集到的数据进行预处理，包括数据清洗、特征提取和特征缩放等步骤。

## PCA降维
使用Python中的PCA库对数据进行主成分分析，以减少特征的数量和相关性

## 滑动窗口处理
使用滑动窗口技术，将数据集划分成多个窗口，并在每个窗口上执行PCA

## 异常检测
在每个窗口上使用PCA处理后的数据，通过设定阈值或其他机器学习模型(如异常检测算法)来检测网络入侵

