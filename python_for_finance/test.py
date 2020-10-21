# coding:utf-8
# Author: luoyu
# Date: 2020/10/15 10:06
# Tool: PyCharm


import numpy as np
import numexpr as ne
from math import *
import time

a = np.arange(25000000)
ne.set_num_threads(4)
f = '3 * log(a) + cos(a) ** 2'
t0 = time.time()
r = ne.evaluate(f)
print('spend %s s' % (time.time() - t0))
print(r)

