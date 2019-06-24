# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年06月21日

from math import log
import operator

def calcShannonEnt(dataSet):
    numData = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        if featVec[-1] not in labelCounts.keys():
            labelCounts[featVec[-1]] = 0
        labelCounts[featVec[-1]] += 1
    ShannonEnt = 0.0
    for key in labelCounts:
        prob = labelCounts[key] / numData
        ShannonEnt -= prob * log(prob,2)
    return ShannonEnt

def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def getBestFeature(dataSet):
    HannonEnt = calcShannonEnt(dataSet)
    InfoGain = 0.0
    numFeaturs = len(dataSet[0]) - 1
    bestFeature = -1
    for i in range(numFeaturs):
        featur_values = [featVec[i] for featVec in dataSet]
        featur_values = set(featur_values)
        new_shannonEnt = 0.0
        for featur_value in featur_values:
            featur_data = splitDataSet(dataSet,i,featur_value)
            featur_shannonEnt = calcShannonEnt(featur_data)
            new_shannonEnt += len(featur_data)/len(dataSet) * featur_shannonEnt
        new_infoGain = HannonEnt - new_shannonEnt
        if new_infoGain > InfoGain:
            InfoGain = new_infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classlist):
    classCount = {}
    for vote in classlist:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = getBestFeature(dataSet)
    bestFeatLable = labels[bestFeat]
    myTree = {bestFeatLable:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    i = 0
    for value in uniqueVals:
        i += 1
        subLables = labels[:]
        myTree[bestFeatLable][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLables)
    return myTree



def createDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels


dataSet,labels = createDataSet()

print(createTree(dataSet,labels))

