'''
迭代
'''
from collections import Iterable

L = [1,2,3,4,5,6,'A','F']
for e in L:     #使用in迭代集合
    print(e)

M = {'a':1,'b':2,'c':3}
for key in M:       #迭代key
    print(key)
for v in M.values():    #迭代value
    print(v)
for key, value in M.items():    #迭代key,value
    print(key,":",value)
# 使用Iterable库来判断对象是否可迭代
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

# 使用下标迭代
for i, v in enumerate(L):
    print(i, v)

# 使用多个参数循环
for x,y in [(1,1), (2,4), (5,9)]:
    print(x, y)
