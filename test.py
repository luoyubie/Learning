# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年05月20日

# importing pandas as pd
import pandas as pd
import numpy as np

# Creating the first dataframe
df1 = pd.DataFrame({"A": [1, 5, 3, 4, 2],
                    "B": [3, 2, 4, 3, 4],
                    "C": [2, 2, 7, 3, 4],
                    "D": [4, 3, 6, 12, 7]},
                   index=["A1", "A2", "A3", "A4", "A5"])
print("df1:\n",df1)

# # Creating the second dataframe
# df2 = pd.DataFrame({"A": [10, 11, 7, 8, 5],
#                     "B": [21, 5, 32, 4, 6],
#                     "C": [11, 21, 23, 7, 9],
#                     "D": [1, 5, 3, 8, 6]},
#                    index=["A1", "A2", "A3", "A4", "A5"])
# print(df2)

# subtract df2 from df1
# df = df1.sub(df2)
# print(df)

sr = pd.Series([12, 25, 64, 18, 10], index=["A1", "A2", "A3", "A4", "A5"])
print("sr:\n",sr)
# Print the series
df_s = df1.sub(sr,axis=0)
print(df_s)

a1 = np.array(df1.values)
a2 = np.array([sr.values]).T
cols = df1.columns
index = df1.index
print(cols)
print(index)
print(a1)
print(a2)
a = a1 - a2
print(a)
print(a>0)
df = pd.DataFrame(a,index=index,columns=cols)
print(df)

df_p = df < 0
print(df_p)
