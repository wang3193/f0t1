'''
https://github.com/jackzhenguo/python-small-examples
'''
## 求绝对值
print(abs(-6))

## 列表元素都为真
print(all([1,2,3,4]))
print(all([1,3,0,-2]))


## 至少一个元素为真
print(any([1,2,0,-1]))
print(any([0,0,[]]))

## ascii展示对象
class Stu():
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'name= '+ self.name

stu = Stu("test")
print(stu)
print(ascii(stu))

# 十进制转二进制
print(bin(11))

# 十进制转八进制
print(oct(9))

# 十转十六进制
print(hex(15))

# 对象转bool
print(bool([1,2,3]))
print(bool([]))

# 字符串转字节
s = "apple"
print(bytes(s, encoding='utf-8'))

# 数值转字符串
i = 100
print(str(i))

# 是否可调用
print(callable(i))
print(callable(str))
print(callable(stu))
# 对象想要被调用需要重写类的__call__方法
class Tea():
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print("this is callable obj")
tea = Tea('teacher')
print(callable(tea))

# 十进制转ascII
print(chr(65))

# ASCII转十进制
print(ord('A'))

# 类方法
'''
使用@classmethod装饰器修饰的函数不需要实例化,不需要self参数,但第一个参数需要是表示自身类的cls参数
可以用来调用类的属性,方法,实例化参数
'''
class User():
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'name= '+ self.name
    @classmethod
    def f(cls, name):
        print(cls(name))
User.f('user')






