import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('stock_details_5_years.csv',sep=',')
print(df.head(10))
print(df.isnull().sum())

dates = pd.to_datetime(df['Date'])
prices = df['High']

# 绘制折线图
plt.plot(dates, prices)

# 设置图表标题和坐标轴标签
plt.title('Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price')

# 自动调整日期标签的格式
plt.gcf().autofmt_xdate()

# 显示图表
plt.show()
