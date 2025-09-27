f=[1,2]
ef=[]
i=3
while max(f) <= 4*10**6:
    f.append(f[i-2] + f[i-3])
    i+=1
for j in f:
    if j%2==0:
        ef.append(j)
print(sum(ef))
