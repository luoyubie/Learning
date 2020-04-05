# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年04月10日


"""
# 斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n<max:
    # 生成器
        yield b
        a,b = b,a+b
        n += 1
    return 'done'

for i in fib(10):
    print(i)
"""

"""
# 具名元组
# 1、创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串
# 2、存放在对应字段里的数据要以一串参数的形式传入到构造函数中
# （注意，元组的构造函数却只接受单一的可迭代对象）。
# 3、你可以通过字段名或者位置来获取一个字段的信息
from collections import namedtuple
City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
# _fields 属性是一个包含这个类所有字段名称的元组
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# 用 _make() 通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟 City(*delhi_data) 是一样的
delhi = City._make(delhi_data)
# _asdict() 把具名元组以 collections.OrderedDict 的形式返回，我们可以利用它来把元组里的信息友好地呈现出来
for key, value in delhi._asdict().items():
    print(key + ':', value)
    
"""

# 不可变的映射类型
from types import MappingProxyType
a = {'a':1,'b':2}
# a_proxy只是一个字典的视图不能修改添加等，a更新则a_proxy会同步更新
a_proxy = MappingProxyType(a)
a['c'] = 3
print(a_proxy)
a.update({'d':4})
print(a_proxy['d'])

