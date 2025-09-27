def func(n, k):
    fk=1
    for i in range(1, n+1):
        fk*=i
    a=k
    count=0
    while fk>a:
        count+=n//a
        a*=k
    return count
n=int(input())
k=int(input())
print(func(n,k))
