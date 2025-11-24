class Node:
    def __init__(sf, data):
        sf.data=data
        sf.next=None
    def print(sf):
        print (sf.data)

class LL:
    def __init__(sf):
        sf.head=None

    def is_empty(sf):
        return sf.head==None

    def append(sf, data):
        newNode=Node(data)
        if sf.is_empty():
            sf.head=newNode
        else:
            curNode=sf.head
            while curNode.next!=None:
                curNode=curNode.next
            curNode.next=newNode

    def prepend(sf, data):
        newNode=Node(data)
        secondNode=sf.head
        sf.head=newNode
        sf.head.next=secondNode

    def delete(sf, data):
        if sf.is_empty():
            return "Error"
        if sf.head.data==data:
            sf.head=sf.head.next
            return "ok"
        lastNode=sf.head
        while lastNode.next.next!=None:
            lastNode=lastNode.next
        if lastNode.next.data==data:
            lastNode.next=None
            return "ok"
        curNode=sf.head
        while curNode.next.data!=data:
            curNode=curNode.next
        curNode.next=curNode.next.next
        return "ok"

    def display(sf):
        curNode=sf.head
        while curNode:
            curNode.print()
            curNode=curNode.next
            
my_linked_list = LL()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.prepend(0)

my_linked_list.display()

my_linked_list.delete(2)

my_linked_list.display()
