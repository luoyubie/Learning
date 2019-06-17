# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年06月04日

import numpy as np
import operator

def creatDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels


def classsify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    # print(inX)
    # print(np.tile(inX,(dataSetSize,1)))
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance ** 0.5
    sortDistance = distances.argsort()
    # print(distances)
    # print(sortDistance)
    classCount = {}
    for i in range(k):
        votelabel = labels[sortDistance[i]]
        classCount[votelabel] = classCount.get(votelabel,0) + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    # print(sortedClassCount)
    return sortedClassCount[0][0]


group,labels = creatDataSet()

print(classsify0([0,0],group,labels,3))
