class Stack:
    def __init__(self):
        self.stack=[]
        return None
    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def push(self, a):
        self.stack.append(a)
        return self.stack
    def pop(self):
        if len(self.stack)!=0:
            return (f'deleted elem is:{self.stack.pop(len(self.stack)-1)}', f'ur len is:{len(self.stack)}')
        else:
            return 'Error, stack shouldn\'t be empty'
    def peek(self):
        if len(self.stack)!=0:
            return self.stack[-1]
        else:
            return 'Error, stack shouldn\'t be empty'
    def size(self):
        return len(self.stack)
myStack=Stack()
print(myStack.is_empty())
print(myStack.push(3))
print(myStack.push(27))
print(myStack.push(52))
print(myStack.is_empty())
print(myStack.peek())
print(myStack.pop())
print(myStack.size())
myStack2=Stack()
print(myStack2.pop())
print(myStack2.peek())
