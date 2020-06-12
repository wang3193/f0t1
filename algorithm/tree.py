#二叉树
class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
    
    def __repr__(self):
        return 'item:'+str(self.item)

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        print("插入数据:", node)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                print(pop_node)
                if pop_node.left is None:
                    pop_node.left = node
                    break
                elif pop_node.right is None:
                    pop_node.right = node
                    break
                else:
                    q.append(pop_node.left) 
                    q.append(pop_node.right)

    def traverse(self):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.item)
            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.item)
        return res

    def preorder(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder(root.left)
        right_item = self.preorder(root.right)
        return result + left_item + right_item
    
    def inorder(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.left)
        right_item = self.preorder(root.right)
        return left_item + result + right_item

    def postorder(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.left)
        right_item = self.preorder(root.right)
        return left_item + right_item + result

t = Tree()
for i in range(10):
    t.add(i)
print(t.traverse())