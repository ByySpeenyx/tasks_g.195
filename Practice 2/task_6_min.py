def func(k1):
    k2=k1+1
    n=1
    while True:
        s1=str(k1*n)
        s2=str(k2*n)
        if sorted(s1)==sorted(s2):
            return n
        n+=1
k=int(input())
print(func(k))
