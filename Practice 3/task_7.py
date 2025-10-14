def func(s, m):
    n=len(s)//2
    lt=int(s[:n])
    rt=int(s[n:])
    return str((lt+rt)**2).zfill(m)
n=int(input())
mxnum=int('9'*n)
r=[]
for i in range(mxnum):
    print(i)
    i=str(i).zfill(n)
    print(i)
    if i==func(i,n):
        r.append(i)
print(r)


