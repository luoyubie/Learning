# coding:utf-8
# Author: luoyu
# Date: 2021/1/31 14:58
# Tool: PyCharm

# 拉格朗日插值法-----------------------------------------------
# import pandas as pd
# from scipy.interpolate import lagrange
#
# pd.set_option('display.max_rows',None)
#
# inputfile = "D:\PycharmProject\\analysis_mining_data\chapter3\demo\data\catering_sale.xls"
# outfile = "D:\PycharmProject\\analysis_mining_data\chapter3\demo\data\sales.xls"
#
# data = pd.read_excel(inputfile)
#
# # # ------------------------------
# # # 直接赋值报SettingWithCopyWarning的警告
# # data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None
# # # ------------------------------
# # 取出符合条件索引 True or False
# mask = (data[u'销量'] < 400) | (data[u'销量'] > 5000)
# data.loc[mask, u'销量'] = None
#
#
# # 拉格朗日插值法 不合理 插值计算有误
# # ToDo python代码编写实现公式再计算
# def ployinterp_column(s, n, k=5):
#     # s为列向量，n为被插值的位置，k为取前后的数据个数
#     # 书中bug，会报out of index 加上reindex
#     s = s.reindex(list(range(n - k, n + 1 + k)))
#     lag_index = list(range(n - k, n)) + list(range(n + 1, n + 1 + k))
#     y = s[lag_index]
#     y = y[y.notnull()]  # 剔除空值
#     lagrange_poly = lagrange(y.index, list(y))
#     # print(type(lagrange_poly))
#     # print("n: {0},result: \n{1}".format(n, lagrange_poly))
#     result = lagrange_poly(n)
#     return result
#
#
# # 逐个元素判断是否需要插值
# # print(data)
# for i in data.columns:
#     for j in range(len(data)):
#         if (data[i].isnull())[j]:
#             # mask =
#             data.loc[j, i] = ployinterp_column(data[i], j)
# print(data)
# data.to_excel(outfile)
# -----------------------------------------------

# 连续属性离散化
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

datafile = 'D:\PycharmProject\\analysis_mining_data\chapter4\demo\data\discretization_data.xls'

data = pd.read_excel(datafile)
data = data[u'肝气郁结证型系数'].copy()
k = 4

# 等宽离散化，各个类比一次命名为0,1,2,3
d1 = pd.cut(data, k, labels=range(k))

# 等频率离散化
w1 = [1.0 * i / k for i in range(k + 1)]
w1 = data.describe(percentiles=w1)[4:4 + k + 1]
print(w1)
w1[0] = w1[0] * (1 - 1e-10)
d2 = pd.cut(data, w1, labels=range(k))

# 基于聚类分析的离散化
from sklearn.cluster import KMeans

kmodel = KMeans(n_clusters=k, n_jobs=4)  # 建立模型，n_jobs是并行数，一般等于cpu数比较好
data1 = np.array(data)
kmodel.fit(data1.reshape(len(data), 1))
# 输出聚类中心，并且排序（默认随机）

c = pd.DataFrame(kmodel.cluster_centers_).sort_values(0)
# 相邻两项求和点作为边界点
# w = pd.rolling_mean(c,2).iloc[1:]
w = c.rolling(2).mean().iloc[1:]
# 把首末边界点加上
w = [0] + list(w[0]) + [data.max()]
d3 = pd.cut(data, w, labels=range(k))


def cluster_plot(d, k):
    plt.figure(figsize=(8, 3))
    for j in range(k):
        plt.plot(data[d == j], [j for i in d[d == j]], 'o')

    plt.ylim(-0.5, k - 0.5)
    return plt


cluster_plot(d1, k).show()
cluster_plot(d2, k).show()
cluster_plot(d3, k).show()
