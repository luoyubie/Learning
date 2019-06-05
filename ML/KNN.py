# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年06月04日

import numpy as np
import operator

def creatDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels


group,labels = creatDataSet()
print(group.shape)
print(labels)


