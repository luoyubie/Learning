# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年03月12日

from math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector(%r,%r)'%(self.x,self.y)


