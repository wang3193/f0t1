'''
位置参数
'''
def power(x):
    return x * x

def power(x, n):
    return x ** n

# 默认参数
def power(x, n= 2):
    return x ** n

# a = power(12)

# 多默认参数
def sign(name, gender, age = 7, address='beijing'):
    print('name:', name, 'age:', age, 'gender:', gender, 'address:', address)

sign('aaa', 'male')
sign('bbb', 'male', address='shanghai')
'''
默认参数要指向不变对象
'''

# 可变参数
'''
可变参数*numbers接收到位一个tuple,允许传入0到N个对象,在函数调用时自动组装为一个tuple
'''
def calc(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

calc(1,2)

# 关键字参数
'''
类似于可变参数,关键字参数将传入的参数组装为一个dict字典
'''

def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)

person('sam',18)
person('sam', 19, city='beijing',gender = 'male')
extra = {'city':'beijing', 'gender': 'male'}
person('sam',18, extra)

# 命名关键字参数
'''
和关键字参数类似,但是只接收定义的关键字参数
'''
def stu(name, age, *, gender, address):
    print('name', name, 'age', age, 'gender', gender, 'address', address)

stu('stu', 18)
stu('stu', 18, gender='male')

# 组合参数
def f1(*args, **kw):
    print('it can receive all args, no matter how it definitions')