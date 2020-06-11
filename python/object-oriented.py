# __slots__ 用于限制示例的属性
class Student(object):
    __slots__ = ('name', 'age') #经允许使用name和age属性

s = Student()
s.name = 'test'
#s.fullname = 'error'

# @property 用于修饰getter方法,创建对应的属性
class Teacher(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if(value == 1):
            self._name = "from setter"
        else:
            self._name = value

t = Teacher()
t.name = 1
print(t.name)
t.name = 2
print(t.name)

# __init__ 初始化类
# __str__ 类似java toString方法,使用print调用时触发
# __repr__ 类似__str__,在直接调用对象时触发
# __iter__ 类似于iterator,用于循环
# __next__ 配合__iter__,获取下一个对象
# __getitem__ 取出元素
# __getattr__ 如果调用的属性不存在时,会调用__getattr__方法
# __call__ 实例对象本身调用方法
