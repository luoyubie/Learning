# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年05月20日

# importing pandas as pd
import pandas as pd

# Creating the first dataframe
df1 = pd.DataFrame({"A": [1, 5, 3, 4, 2],
                    "B": [3, 2, 4, 3, 4],
                    "C": [2, 2, 7, 3, 4],
                    "D": [4, 3, 6, 12, 7]},
                   index=["A1", "A2", "A3", "A4", "A5"])
print(df1)

# Creating the second dataframe
df2 = pd.DataFrame({"A": [10, 11, 7, 8, 5],
                    "B": [21, 5, 32, 4, 6],
                    "C": [11, 21, 23, 7, 9],
                    "D": [1, 5, 3, 8, 6]},
                   index=["A1", "A2", "A3", "A4", "A5"])
# print(df2)

# subtract df2 from df1
df = df1.sub(df2)
# print(df)

sr = pd.Series([12, 25, 64, 18], index=["A", "B", "C", "D"])
print(sr)
# Print the series
df_s = df1.sub(sr,axis=1)
print(df_s)

