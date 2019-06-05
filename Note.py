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











