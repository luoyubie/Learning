# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年05月20日


# python反射机制 -- 文件内通过字符串调用函数
import sys
moudle = sys.modules[__name__]
fun1 = getattr(moudle,'文件内的函数名')

# python反射机制 从其他模块通过 函数名(string)调用函数
md = __import__("模块名",fromlist=True)
fun2 = getattr(md,"函数名")

# H5相关
import os
import re
from tables import *
import pandas as pd
from pandas import DataFrame
import datetime
import time



# 实现一个优先队列
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


# __init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
# __new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。
# 即，__new__在__init__之前被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数


# 如果是直接执行py文件，则__name__的值为__main__；
# 如果是以导入模块的形式执行py文件，则__name__的值为该py文件的文件名
# __name__的目的就是如果是以导入模块的形式执行文件，不会执行if __name__ == '__main__'下面的语句




