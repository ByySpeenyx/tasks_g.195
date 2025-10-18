def bins(x, tar):
    mid=len(x)//2
    if tar==x[mid]:
        return mid
    if tar not in x:
        return -1
    if tar < x[mid]:
        x=x[:mid]
        return bins(x, tar)
    else:
        x=x[mid:]
        return bins(x, tar)
print(bins([1, 2, 3, 4, 5, 6, 7], 4))
 
