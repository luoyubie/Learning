# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2020年06月25日

import random
class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    # 类定义了__call__ 方法，那么他的实例可以作为函数调用
    def __call__(self):
        return self.pick()

bingo = BingoCage(range(10))
# 以下两种调用方法效果一样
print(bingo.pick())
print(bingo())

# -----------------------------------------

# tag函数用于生成HTML标签
# cls为仅限关键字参数
def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

# print(tag('tr',*['a','b'],cls='ppp'))
# print(tag('p', 'hello', 'world'))
# print(tag('p', 'hello', id=33))

# ------------------------------------------------

from functools import reduce

def fact(n):
    return reduce(lambda a,b: a*b, range(1,n+1))

# print(fact(5))
# ------------------------------------------------

from operator import itemgetter

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

# c_name = itemgetter(1,0)
# print(c_name(metro_data))
# for i in metro_data:
#     print(c_name(i))

#-----------------------------------------

from collections import namedtuple

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name,cc,pop,LatLong(lat,long))
               for name,cc,pop,(lat,long) in metro_data]
# print(metro_areas[0].coord.lat)

from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat')
# for city in sorted(metro_areas,key=attrgetter('coord.lat'),reverse=True):
#     print(name_lat(city))
