class Q:
    def __init__(self):
        self.q = []
    
    def sort_q(self):
        r = []
        for i in range(6):
            for j in self.q:
                if j[1] == i: 
                    r.append(j) 
        return r
    
    def empty(self):
        return len(self.q) == 0

    def enq(self, item, priority=5):  
        self.q.append((item, priority))  
        return self.sort_q()
    
    def deq(self): 
        if self.empty():
            return 'queue is empty'
        deleted_elem = self.q.pop(0)
        return f'deleted elem: {deleted_elem}', f'ur queue: {self.q}'
    
    def size(self):
        return len(self.q)

    def front(self):
        if not self.empty():  
            return self.q[0] 
        else:
            return 'queue shouldn\'t be empty'

myq = Q()
print("empty:", myq.empty())
print("enq(1, 2):", myq.enq(1, 2))
print("enq(2):", myq.enq(2, 5)) 
print("enq(3, 0):", myq.enq(3, 0))
print("deq:", myq.deq())
print("front:", myq.front())
print("empty:", myq.empty())
print("size:", myq.size())
