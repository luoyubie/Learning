# _*_ encoding:utf-8 _*_
"""
@file test1.py
@author : luoyu_bie
@time 2019-06-17
"""

import numpy as np
import operator

def creatDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels


def classify0(inX,dataSet,labels,k):
    dataSetsize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetsize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    distances = sqDiffMat.sum(axis=1)
    sortedDistances = distances.argsort()
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistances[i]]
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    print(classCount)
    sortedclassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    print(sortedclassCount)
    return sortedclassCount[0][0]

inX = [0,0]
dataSet,labels = creatDataSet()
print(classify0(inX,dataSet,labels,3))

