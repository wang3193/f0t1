''' 量化交易
国内平台: BigQuant 果仁网
国外: Quantopian
'''
import matplotlib.pyplot as plt
import pandas as pd
import requests

# 选择要获取的数据时间段
periods = '3600'

# 抓取btc 历史价格数据

resp = requests.get('http://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
                params= {
                    'periods': periods
                })
data = resp.json()

# 转换成 pandas data frame
df = pd.DataFrame(data['result'][periods],
                columns = [
                    'CloseTime',
                    'OpenPrice',
                    'HighPrice',
                    'LowPrice',
                    'ClosePrice',
                    'Volume',
                    'NA'
                ])

# 输出 DataFrame 的头部几行
print(df.head())

# 绘制 btc 价格曲线
df['ClosePrice'].plot(figsize=(14, 7))
plt.show()