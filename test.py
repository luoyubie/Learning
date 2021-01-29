# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年05月20日

import pandas as pd
import numpy as np
import copy

a = [1,2,3,[1,2,3]]
b = copy.deepcopy(a)
print(a)
b[-1][0] = 10
print(a)


