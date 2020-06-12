class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        #判断列表是否为null
        return self._head == None

    def length(self):
        #返回链表长度
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        #遍历链表
        cur = self._head
        while cur != None:
            print(cur.item) 
            cur = cur.next

    def add(self, item):
        # 头部插入元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
    
    def append(self, item):
        # 尾部插入元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
    
    def search(self, item):
        # 查找元素是否存在
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    
    def insert(self, pos, item):
        # 指定位置添加节点
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            for i in range(1, pos - 1):
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        # 删除元素
        if self.is_empty:
            return
        cur = self._head
        while cur != None:
            if cur.item == item:
                if cur.prev == None:
                    #前节点为null
                    if cur.next == None:
                        #厚街店为null,说明当前只有一个元素,为_head元素
                        self._head = None
                        break
                    else:
                        self._head = cur.next
                        self._head.prev = None
                        break
                elif cur.next == None:
                    cur.prev.next = None
                    break
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
            cur = cur.next



d = DLinkList()
d.append("1")
d.append("2")
d.append("3")
d.append("4")
d.insert(3, "5")
d.travel()
print("=========================")
d.remove('4')
d.travel()
print("=========================")
d.remove('1')
d.travel()
print("=========================")
d.remove('5')
d.travel()
print("=========================")