def func(n):
    if n>0:
        fack=1
        for i in range(1,n+1):
            fack*=i
        return f'"{fack}"'
    elif n==0:
        return f'"1"'
    else:
        return None
n=int(input())
print(func(n))
