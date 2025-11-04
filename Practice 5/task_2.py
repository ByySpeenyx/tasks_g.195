from itertools import*
def func(a):
    k=0
    for i in permutations(a):
        k+=1
    return k
print(func({"rose", "jasmine", "lily"}))
print(func({"orchid", "tulip", "violet", "daisy"}))
print(func({"lavender", "sunflower"}))
