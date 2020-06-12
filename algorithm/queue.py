class Queue(object):
    __slots__ = ('__queue')

    def __init__(self):
        self.__queue = []

    def __repr__(self):
        return str(self.__queue)

    def inqueue(self, item):
        # 入队
        self.__queue.append(item)

    def manyInQueue(self, *args):
        # 批量入队
        self.__queue.extend(args)

    def outQueue(self):
        #出队
        if not self.__queue == []:
            self.__queue.pop(0)
        else:
            return None
    
    def show(self):
        for i in self.__queue:
            print(i) 
    
    def head(self):
        if not self.__queue == []:
            print(self.__queue[0])
        else:
            return None
    
    def tail(self):
        if not self.__queue == []:
            print(self.__queue[-1])
        else:
            return None

    def isEmpty(self):
        return self.__queue == []

    def length(self):
        print(len(self.__queue))


q = Queue()
q.inqueue(1)
q.manyInQueue(2,3,4,5)
print(q)
q.head()
q.length()
q.tail()
q.outQueue()
q.head()