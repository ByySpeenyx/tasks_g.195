class KeyValuePair:
    def __init__(sf, key, value):
        sf.key=key
        sf.value=value
class UnorderedMap:
    def __init__(sf, size=10):
        sf.size=size
        sf.buckets=[[] for _ in range(size)]

    def hash(sf, key):
        return len(key)%sf.size

    def set(sf,key, value):
        newBt=KeyValuePair(key, value)
        i=sf.hash(key)
        if sf.buckets[i]:
            for pair in sf.buckets[i]:
                if pair.key==key:
                    pair.value=value
                    return
            sf.buckets[i].append(newBt)
        else:
            sf.buckets[i].append(newBt)

    def get(sf, key, default = None):
        i=sf.hash(key)
        if sf.buckets[i]:
            for pair in sf.buckets[i]:
                if pair.key==key:
                    return pair.value
            return default
        else:
            return default

    def remove(sf, key):
        i=sf.hash(key)
        if sf.buckets[i]:
            for pair in sf.buckets[i]:
                if pair.key==key:
                    sf.buckets[i].remove(pair)
                    return
            return "there is no key in map"

    def keys(sf):
        r=[]
        for i in sf.buckets:
            for pair in i:
                r.append(pair.key)
        return r

    def values(sf):
        r=[]
        for i in sf.buckets:
            for pair in i:
                r.append(pair.value)
        return r

    def items(sf):
        r=[]
        for i in sf.buckets:
            for pair in i:
                r.append((pair.key, pair.value))
        return r
my_map = UnorderedMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())
