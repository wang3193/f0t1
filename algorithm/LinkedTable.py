class Node(object):
    '''
   data: 数据
   _next: 节点对象
    '''
    def __init__(self, data, pnext=None):
       self.data = data
       self._next = pnext

    
    def __repr__(self):
        return str(self.data)


class ChainTable(object):
    def __init__(self):
        self.head = Node('header')
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataOrNode) :
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        
        node = self.head
        while node._next:
            node = node._next
        node._next = item
        self.length += 1


chain = ChainTable()