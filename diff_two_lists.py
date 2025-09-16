a=[int(input()) for i in range(5)]
print(a)
b=[int(input()) for i in range(3)]
print(b)
for i in b:
    if i in a:
        while i in a:
            a.remove(i)
print(a)
