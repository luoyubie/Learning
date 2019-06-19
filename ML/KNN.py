# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年06月04日

import numpy as np
import operator
import os

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


def file2matrix(filename):
    fr = open(filename)
    arrayOlines = fr.readlines()
    line_num = len(arrayOlines)
    returnMat = np.zeros((line_num,3))
    index = 0
    classLable = []
    for line in arrayOlines:
        line = line.strip()
        listfromline = line.split('\t')
        returnMat[index,:] = listfromline[:3]
        classLable.append(int(listfromline[-1]))
        index += 1
    return returnMat,classLable

def autoNorm(dataSet):
    # 数据归一化处理
    m = dataSet.shape[0]
    minVal = dataSet.min(0)
    maxVal = dataSet.max(0)
    minVal_Set = np.tile(minVal,(m,1))
    ranges = maxVal - minVal
    ranges_Set = np.tile(ranges,(m,1))
    norm_Set = (dataSet - minVal_Set)/(ranges_Set)
    return norm_Set


def datingClassTest():
    hoRatio = 0.1
    filename = "E:\code\Learning\ML\Data\Ch02\datingTestSet2.txt"
    returnMat, classLable = file2matrix(filename)
    normSet = autoNorm(returnMat)
    m = normSet.shape[0]
    testNum = int(hoRatio * m)
    error_num = 0.0
    for i in range(testNum):
        result_label = classsify0(normSet[i,:], normSet[testNum:m,:], classLable[testNum:m], 5)
        print("The classifier came back with %s,The real label is %s" % (result_label,classLable[i]))
        if result_label != classLable[i]:
            error_num += 1
    print("The classifier error ratio is %f" % (error_num/float(testNum)))

def img2vec(filename):
    returnVector = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        line = fr.readline()
        for j in range(32):
            returnVector[0,i*32+j] = int(line[j])
    return returnVector

def _get_Vec(path):
    filenames = os.listdir(path)
    labels = []
    file_num = len(filenames)
    dataSet = np.zeros((file_num, 1024))
    for i in range(file_num):
        filename = filenames[i]
        labels.append(filename[0])
        filepath = os.path.join(path, filename)
        vec = img2vec(filepath)
        dataSet[i, :] = vec
    return dataSet,labels

def Digital_Recognition():
    path_train = "E:\code\Learning\ML\Data\Ch02\\trainingDigits"
    train_dataSet,train_labels = _get_Vec(path_train)
    path_test = "E:\code\Learning\ML\Data\Ch02\\testDigits"
    test_dataSet,test_labels = _get_Vec(path_test)
    error_num = 0.0
    for i in range(test_dataSet.shape[0]):
        predict_label = classsify0(test_dataSet[i,:],train_dataSet,train_labels,3)
        print("The classifier came back label is %s,The real label is %s"%(predict_label,test_labels[i]))
        if predict_label != test_labels[i]:
            error_num += 1
    print("The classifier error ratio is %f" % (error_num/float(len(test_labels))))


if __name__ == "__main__":
    # datingClassTest()
    Digital_Recognition()


















