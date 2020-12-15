# coding:utf-8
# Author: luoyu
# Date: 2020/10/15 10:06
# Tool: PyCharm

import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt

# 600018.SS
yahoo = web.DataReader('000001.SS', data_source='yahoo', start=dt.datetime(2019,1,1),end=dt.date.today())


# 计算波动率
yahoo['Log_Ret'] = np.log(yahoo['Close'] / yahoo['Close'].shift(1))
yahoo['Volatility'] = yahoo['Log_Ret'].rolling(window=252).std() * np.sqrt(252)
print(yahoo)

yahoo.dropna(how='any',inplace=True)
plt.figure()
plt.subplot(2,1,1)
plt.plot(yahoo['Volatility'])
plt.subplot(2,1,2)
plt.plot(yahoo['Close'])
plt.show()








