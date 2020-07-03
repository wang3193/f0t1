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

# 执行字符串表示的代码
s = "print('hello world')"
r = compile(s, "<string>", "exec")
exec(r)

# 创建复数
print(complex(1, 2))

# 动态删除对象属性
delattr(tea, 'name')
print(hasattr(tea, 'name'))

# 转为字典
dict1 = dict(a='a', b='2')
dict2 = dict([('a',3), ('b', 5)])
print(dict1)
print(dict2)

# 查看对象所有方法
print(dir(stu))

# 取商和余数
print(divmod(10,3))

# 枚举对象
s = ['a', 'b', 'c']
for i, v in enumerate(s, 1):
    print(i, v)

# 计算表达式:
s = "1+2+3"
print(eval(s))

# 查看变量所占字节数
import sys
print(sys.getsizeof(s))

# 过滤器
fil = filter(lambda a: a > 10, [1,10,2,9,11,15])
print(list(fil))

# 整数转成浮点数
print(float(3))

# 字符串格式化
print("i am {0}, arg2 is {1}".format("sam", 110))

# 创建不可修改的set
print(frozenset([1,2,1,3,4,3]))

# 返回对象的hash值
print(hash(tea))

# 帮助文档
# print(help(tea))

# 获取用户输入
# input()

# 读取文件
'''
fo = open(path, mode, encoding)
fo.read()
mode 取值范围
'r'	读取（默认）
'w'	写入，并先截断文件
'x'	排它性创建，如果文件已存在则失败
'a'	写入，如果文件存在则在末尾追加
'b'	二进制模式
't'	文本模式（默认）
'+'	打开用于更新（读取与写入）
'''

# 次幂
print(pow(2,3))
print(pow(2,3,5))   #取余

# 返回对象内存地址
print(id(stu))

# 反向迭代器
rev = reversed([1,2,3,4,5])
for i in rev:
    print(i)

# 四舍五入
print(round(3.1415926, 2))

# 转化为集合
a = [1,2,2,3,4,3,5]
print(set(a))

# 切片对象
a = [1,2,3,4,5,6,7,8,9,1,2,3,4,5]
my_slice = slice(0, 9, 3)  #slice(start, end, step)
print(a[my_slice])

# 排序函数
print(sorted(a, reverse=True)) # sorted(array, key, reverse)

# 求和函数
print(sum(a))

# 转元祖
print(tuple(a))

# 查看对象类型
print(type([1,2,3]))

# 动态方法
from operator import *

def calc(a, b, op): 
    return {
        '+': add,
        '-': sub,
        '*': mul,
        '**': pow,
        '/': truediv
    }[op](a,b)

print(calc(1,2,'+'))

# swap
a = 2
b = 3
a,b = b,a
print("a:",a, "b:", b)

