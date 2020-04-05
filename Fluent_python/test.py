# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年03月12日

from types import MappingProxyType

a = {'a':1,'b':2}

a_proxy = MappingProxyType(a)
a['c'] = 3
print(a_proxy)
a.update({'d':4})
print(a_proxy['d'])


