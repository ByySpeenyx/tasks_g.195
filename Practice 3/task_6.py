n=int(input())
m=int(input())
a=[int(input()) for i in range(n)]
for i in range(m):
    q1=int(input())
    q2=int(input())
    qq=a[q1:q2]
    mx=0
    for j in qq:
        if qq.count(j)>mx:
            mx=qq.count(j)
    print(mx)
