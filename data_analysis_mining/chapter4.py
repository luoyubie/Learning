# coding:utf-8
# Author: luoyu
# Date: 2021/1/31 14:58
# Tool: PyCharm

# 拉格朗日插值法-----------------------------------------------
# import pandas as pd
# from scipy.interpolate import lagrange
#
# # pd.set_option('display.max_rows',None)
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
