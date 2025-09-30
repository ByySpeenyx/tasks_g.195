def func(a):
    m=[]
    pos=0
    neg=0
    zer=0
    mx=0
    for i in a:
        if i > 0:
            pos+=1
        if i < 0:
            neg+=1
        if i == 0:
            zer+=1
    if pos == len(a):
        return sum(a)
    elif neg == len(a):
        return 0
    elif zer == len(a):
        return 0
    else:
        for i in range(len(a)-1):
            if len(m)==0:
                if a[i]+a[i+1]>1:
                    m.append(a[i])
            else:
                if sum(m)+a[i]>1:
                    m.append(a[i])
                else:
                    mx=sum(m)
                    m=[]
    return mx                
n=int(input())
a=[int(input()) for i in range(n)]
print(func(a))

