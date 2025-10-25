from random import*
def dek(x):
    if len(x)<=4:
        return sorted(x)
    else:
        pivot=randint(1, max(x))
        lt=[]
        rt=[]
        for i in x:
            if i>pivot:
                rt.append(i)
            elif i<=pivot:
                lt.append(i)
        return (dek(lt)+dek(rt))
print(dek([4, 2, 7, 1, 3, 5]))
print(dek([10, 5, 3, 8]))
print(dek([1]))
print(dek([3, 2]))
print(dek([7, 3, 3, 4, 1, 2, 5]))

