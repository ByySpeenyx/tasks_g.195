mx=0
r=[]
for i in range(2,1000):
    n=1/i
    n=str(n)[2:]
    for j in range(2,1000):
        if n.count(str(j))>mx:
            mx=n.count(str(j))
            if len(r)==0:
                r.append(i)
            else:
                r.remove(r[0])
                r.append(i)
print(r[0])
