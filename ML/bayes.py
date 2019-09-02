# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年07月11日

import numpy as np


def loadDataSet():
    # 测试数据
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    # 分类标签
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

def createVocabList(dataSet):
    # 获取所有单词的不重复列表
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
    """

    :param vocabList: 所有单词的不重复列表
    :param inputSet: 需要分类的单词列表
    :return:
    """
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word：%s is not in my Vocabulary!" % word)
    return returnVec


def train_nb0(train_matrix,train_category):
    num_traindocs = len(train_matrix)
    num_words = len(train_matrix[0])
    p_abusive = sum(train_category) / float(num_traindocs)
    p0_num = np.zeros(num_words)
    p1_num = np.zeros(num_words)
    p0_denom = 0.0
    p1_denom = 0.0
    for i in range(num_traindocs):
        if train_category[i] == 1:
            p1_num += train_matrix[i]
            p1_denom += sum(train_matrix[i])
        else:
            p0_num += train_matrix[i]
            p0_denom += sum(train_matrix[i])
    p1_vect = p1_num / p1_denom
    p0_vect = p0_num / p0_denom
    return p0_vect,p1_vect,p_abusive





if __name__ == "__main__":
    listOPosts,listClasses = loadDataSet()
    # print(listOPosts)
    # print(listClasses)
    myVocabList = createVocabList(listOPosts)
    # print(myVocabList)
    # print(setOfWords2Vec(myVocabList,listOPosts[1]))
    train_mat = []
    for post_in_doc in listOPosts:
        train_mat.append(setOfWords2Vec(myVocabList,post_in_doc))
    print(train_mat)
    p0v,p1v,pAb = train_nb0(train_mat,listClasses)
    print(p0v)
    print(p1v)
    print(pAb)






