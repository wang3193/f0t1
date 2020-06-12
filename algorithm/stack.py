class Stack(object):
    #栈
    __slots__ = ('__items')

    def __repr__(self):
        return str(self.__items)

    def __init__(self):
        self.__items = []
    
    def is_empty(self):
        return self.__items == []

    def peek(self):
        #返回栈顶元素
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)
    
    def push(self, item):
        #入栈
        self.__items.append(item)

    def pop(self):
        #出栈
        return self.__items.pop()

stock = Stack()
stock.push('a')
stock.push('b')
stock.push('c')
print(stock.size())
print(stock.peek())
print(stock)
print(stock.pop())
print(stock)