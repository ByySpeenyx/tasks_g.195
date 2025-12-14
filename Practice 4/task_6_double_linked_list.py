class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class double_linked_list:
    def __init__(self):
        self.root=None

    def append(self, data):
        newnode=Node(data)
        if self.root==None:
            self.root=newnode
        else:
            curnode=self.root
            while curnode.next is not None:
                curnode=curnode.next
            curnode.next=newnode
            newnode.prev=curnode
    
    def prepend(self, data):
        newnode=Node(data)
        if self.root is None:
            self.root=newnode
        else:
            curnode=self.root
            self.root=newnode
            curnode.prev=self.root
            self.root.next=curnode

    def delete(self, data):
        curnode=self.root
        if curnode.data==data:
            self.root=self.root.next
        else:
            while curnode.data!=data:
                curnode=curnode.next
            curnode.next.prev=curnode.prev
            curnode.prev.next=curnode.next
    
    def display(self):
        curnode=self.root
        print(self.root.data)
        while curnode.next is not None:
            print(curnode.next.data)
            curnode=curnode.next
        print("\n")

    def display_reverse(self):
        curnode=self.root
        while curnode.next is not None:
            curnode=curnode.next
        while curnode.prev is not None:
            print(curnode.data)
            curnode=curnode.prev
        print(curnode.data)
        print("\n")

# Пример использования
dll = double_linked_list()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()  # Ожидаемый вывод: 1 <-> 2 <-> 3 <-> None

dll.prepend(0)
dll.display()  # Ожидаемый вывод: 0 <-> 1 <-> 2 <-> 3 <-> None

dll.delete(2)
dll.display()  # Ожидаемый вывод: 0 <-> 1 <-> 3 <-> None

dll.display_reverse()  # Ожидаемый вывод: 3 <-> 1 <-> 0 <-> None
