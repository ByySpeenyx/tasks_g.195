class SimpleMap:
    def __init__(self):
        self.items=[]

    def set(self, key, value):
        pair=[key, value]
        # pair.append(key)
        # pair.append(value)
        if self.items:
            for i in self.items:
                if i[0]==key:
                    return
        self.items.append(pair)

    def get(self, key, default=None):
        for i in self.items:
            if i[0]==key:
                return i[1]
        return default

    def remove(self, key):
        for i in self.items:
            if i[0]==key:
                self.items.remove(i)
        return None

    def keys(self):
        r=[]
        for i in self.items:
            r.append(i[0])
        return r

    def values(self):
        r = []
        for i in self.items:
            r.append(i[1])
        return r

    def Items(self):
        return self.items

my_map = SimpleMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.Items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())
