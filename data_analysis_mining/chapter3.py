# coding:utf-8
# Author: luoyu
# Date: 2021/1/20 21:31
# Tool: PyCharm


# -------------------------
import pandas as pd
import matplotlib.pyplot as plt

atering_sale = "D:\PycharmProject\\analysis_mining_data\chapter3\demo\data\catering_sale.xls"

data = pd.read_excel(atering_sale)
print(data.describe())
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
p = data.boxplot(return_type='dict')
print(p)
x = p['fliers'][0].get_xdata()  # fliers为异常值的标签
y = p['fliers'][0].get_ydata()
y.sort()
for i in range(len(x)):
    if i > 0:
        # plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))
plt.show()
# --------------------------

catering_sale = "D:\PycharmProject\\analysis_mining_data\chapter3\demo\data\catering_sale_all.xls"
data = pd.read_excel(catering_sale, index_col=u'日期')
# print(data)

# 相关系数矩阵，即给出了任意两款菜式之间的相关系数
corr_df = data.corr()
print(corr_df)

print(corr_df.loc[u'百合酱蒸凤爪', u'翡翠蒸香茜饺'])
print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']))

# ----------------------
# 饼图
import matplotlib.pyplot as plt

labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()

# ----------------------------------
