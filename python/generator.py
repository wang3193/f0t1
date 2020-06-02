'''
列表生成器
'''
L1 = list(range(1,11))
print(L1)
# 表达式生成列表
L2 = [x*x for x in range(1,11)]
print(L2)
# 双层循环,笛卡尔积
L3 = [x+n for x in range(1, 51) if x % 5 == 0 for n in range(1, 10)]
print(L3)
'''
打印结果:[6, 7, 8, 9, 10, 11, 12, 13, 14, 11, 12, 13, 14, 15, 16, 17, 18, 19, 16, 17, 18, 19, 20, 21, 22, 23, 24, 21, 22, 23, 24, 25,
26, 27, 28, 29, 26, 27, 28, 29, 30, 31, 32, 33, 34, 31, 32, 33, 34, 35, 36, 37, 38, 39, 36, 37, 38, 39, 40, 41, 42, 43, 44, 41, 42, 43, 44, 45, 46, 47, 48, 49, 46, 47, 48, 49, 50, 51, 52, 53, 54, 51, 52, 53, 54, 55, 56, 57, 58, 59]
'''
# 带if的生成器,注意不能使用else
L4 = [x for x in range(1, 31) if x % 3 == 0]
print(L4)

# 如果for前带if则一定要添加else,因为for前是一个表达式,需要else来判断结果,
L5 = [x if x % 2== 0 else -x for x in range(1,10)]
print(L5)

'''
生成器,按需生成列表,推算后续元素
'''
G1 = (x for x in range(0, 100))
print(next(G1))
print(next(G1))
print(next(G1))

#为方法添加yeild关键字将方法变为生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'
for n in fib(6):
    print(n)
#使用for循环无法拿到return的数据,如果要获取return的值需要使用next()并捕获StopIteration错误
g = fib(6)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break

