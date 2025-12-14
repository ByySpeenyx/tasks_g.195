class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def _hash(self, key):
        return hash(key)%self.size

    def put(self, key, value):
        i=self._hash(key)
        if key in self.slots:
            self.data[i]=vaulue
        elif self.slots[i]!= None:
            i+=1
            self.size+=1
            self.slots.insert(-1, None)
            self.data.insert(-1, None)
            self.slots[i]=key
            self.data[i]=value
        else:
            self.data[i]=value
            self.slots[i]=key
    def get(self, key, default=None):
        i=self._hash(key)
        if  key in self.slots:
            return self.data[i]
        else:
            return default


    def remove(self, key):
        i=self.slots.index(key)
        self.data[i]=None
        self.slots[i]=None

    def keys(self):
        r=[]
        for i in self.slots:
            if i != None:
                r.append(i)
        return r



    def values(self):
        r = []
        for i in self.data:
            if i != None:
                r.append(i)
        return r


    def items(self):
        r=[]
        for i in range(self.size):
            rr=[]
            if self.slots[i]!=None:
                rr.append(self.slots[i])
            if self.data[i]!=None:
                rr.append(self.data[i])
            if rr:
                r.append(rr)
        return r
# Пример использования
my_hashmap = HashMap()
my_hashmap.put("name", "John")
my_hashmap.put("age", 25)
my_hashmap.put("city", "Example City")
print("Keys:", my_hashmap.keys())  # Ожидаемый вывод: Keys: ['name', 'age', 'city']
print("Values:", my_hashmap.values())  # Ожидаемый вывод: Values: ['John', 25, 'Example City']
print("Items:",
      my_hashmap.items())  # Ожидаемый вывод: Items: [('name', 'John'), ('age', 25), ('city', 'Example City')]

# Доступ к значениям по ключу
print("Name:", my_hashmap.get("name"))  # Ожидаемый вывод: Name: John
print("Gender:", my_hashmap.get("gender", "Not specified"))  # Ожидаемый вывод: Gender: Not specified

# Удаление пары ключ-значение
my_hashmap.remove("age")
print("Keys after removing 'age':", my_hashmap.keys())  # Ожидаемый вывод: Keys after removing 'age': ['name', 'city']
