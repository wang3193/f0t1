'''
大型回测框架
 Zipline 热门的事件驱动回测框架
 PyAlgoTrade 事件驱动回车框架,不支持pandas模块和对象
'''
import os
import pandas as pd

def assert_msg(condition, msg):
    if not condition:
        raise Exception(msg)

def read_file(filename):
    # 获取文件绝对路径
    filepath = os.path.join(os.path.dirname(__file__), filename)

    # 判断文件是否存在
    assert_msg(os.path.exists(filepath), "文件不存在")

    # 读取csv文件并返回
    return pd.read_csv(filepath,
                        index_col = 0,
                        parse_dates = True,
                        infer_datetime_format = True)

BTCUSD = read_file('c:/file/tmp/BTCUSD_GEMINI.csv')
assert_msg(BTCUSD.__len__() > 0 , '读取失败')
print(BTCUSD.head())