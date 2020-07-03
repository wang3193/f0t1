# 字符串操作和正则

# 翻转字符串
a = "123"
print(''.join(reversed(a)))
print(a[::-1])

# 使用join连接字符
arr = ['1', '5', 'aaa', 'T']
print(','.join(arr))

# 字符串的字节长度
def str_len(my_str):
    return (len(my_str.encode('utf-8')))
print(str_len('abcdse'))

# 正则
import re

# 查找第一个匹配串
s = "i love this game"
c = 'love'
r = re.search(s, c)
print(r)

# 查找所有匹配的字符串索引
s = "i love this game and that game, and game is the last game"
c = "game"
r = re.finditer(s, c)
for i in r:
    print(i)

# 匹配数字
s = "abc1h32k5hk34k56"
p = r'\d+'
r = re.findall(s, p)
print(r)

# 匹配浮点数
s = "20hadad1.342sda.0.darwqe.0.123sda"
p = r'\d+\.?\d+|\d+'
r = re.findall(s, p)
print(r)