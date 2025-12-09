class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert_rec(self, curnode, node):
        if node.data>curnode.data:
            if curnode.right is None:
                curnode.right=node
            else:
                self.insert_rec(curnode.right, node)
        else:
            if curnode.left is None:
                curnode.left=node
            else:
                self.insert_rec(curnode.left, node)
        
    def insert(self, data):
        newnode=TreeNode(data)
        if self.root is None:
            self.root=newnode
        else:
            curnode=self.root
            self.insert_rec(curnode, newnode)

    def search_rec(self, curnode, data):
        if curnode.data==data:
            return True
        elif data!=curnode.data and (curnode.left is None and curnode.right is None):
            return False
        elif curnode.data<data:
            return self.search_rec(curnode.right, data)
        else:
            return self.search_rec(curnode.left, data)
    def search(self, data):
        curnode=self.root
        return self.search_rec(curnode, data)
    
    def Rin_order_traversal(self, curnode, r):
        if curnode is None:
            return 
        self.Rin_order_traversal(curnode.left, r)
        r.append(curnode.data)
        self.Rin_order_traversal(curnode.right, r)
        return r
    def in_order_traversal(self):
        r=[]
        curnode=self.root
        self.Rin_order_traversal(curnode, r)
        return r
    
    def Rpre_order_traversal(self, curnode, r):
        if curnode is None:
            return
        r.append(curnode.data)
        self.Rpre_order_traversal(curnode.left, r)
        self.Rpre_order_traversal(curnode.right, r)
        return r
    
    def pre_order_traversal(self):
        curnode=self.root
        r=[]
        self.Rpre_order_traversal(curnode, r)
        return r
    
    def Rpost_order_traversal(self, curnode, r):
        if curnode is None:
            return 
        self.Rpost_order_traversal(curnode.left, r)
        self.Rpost_order_traversal(curnode.right, r)
        r.append(curnode.data)
        return r
    
    def post_order_traversal(self):
        curnode=self.root
        r=[]
        self.Rpost_order_traversal(curnode, r)
        return r
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.search(5))  # Ожидаемый вывод: <__main__.TreeNode object at ...>
print(tree.search(20))  # Ожидаемый вывод: None

print(tree.in_order_traversal())  # Ожидаемый вывод: [5, 10, 15]
print(tree.pre_order_traversal())  # Ожидаемый вывод: [10, 5, 15]
print(tree.post_order_traversal())  # Ожидаемый вывод: [5, 15, 10]
