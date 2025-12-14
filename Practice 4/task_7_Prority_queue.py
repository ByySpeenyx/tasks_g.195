class PriorityQueue:
    def __init__(self):
        self.elements=[]

    def is_empty(self):
        return len(self.elements)==0
    
    def push(self, item, priority):
        self.elements.append((item, priority))
        self.elements=self.sort(self.elements)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop(-1)
        else:
            return False
    
    def peek(self):
        if not self.is_empty():
            return (self.elements[-1])
    
    def sort(self, arr):
        priorities=[]
        res=[]
        for i in arr:
            if i[1] not in priorities:
                priorities.append(i[1])
        priorities=sorted(priorities, reverse=True)
        for i in priorities:
            for j in arr:
                if j[1]==i:
                    res.append(j)
        return res
    def size(self):
        return len(self.elements)
    

pq = PriorityQueue()

pq.push("Задача 1", priority=2)
pq.push("Задача 2", priority=5)
pq.push("Задача 3", priority=1)

print("Первый элемент с наивысшим приоритетом:", pq.peek())  # Ожидаемый вывод: Задача 3

while not pq.is_empty():
    print("Обработка:", pq.pop())
