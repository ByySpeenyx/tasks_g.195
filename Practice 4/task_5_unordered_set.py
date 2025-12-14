class UnorderedSet:
    def __init__(self, size=10):
        self.size=size
        self.buckets=[[] for _ in range(size)]

    def _hash(self, value):
        return value % self.size

    def add(self, value):
        i=self._hash(value)
        for j in self.buckets[i]:
            if j==value:
                print( "value already in set")
        self.buckets[i].append(value)

    def remove(self, value):
        i=self._hash(value)
        if value in self.buckets[i]:
            self.buckets[i].remove(value)
        else:
            print( "value not in set")

    def contains(self, value):
        i=self._hash(value)
        if value in self.buckets[i]:
            return True
        else:
            return False

    def elements(self):
        r=[]
        for i in self.buckets:
            for j in i:
                r.append(j)
        return r
my_set = UnorderedSet()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print("Elements:", my_set.elements())

# Check if a value is in the set
value_to_check = 2
print(f"Is {value_to_check} in the set? {my_set.contains(value_to_check)}")

# Remove a value from the set
value_to_remove = 1
my_set.remove(value_to_remove)

print("Elements after removing 1:", my_set.elements())
