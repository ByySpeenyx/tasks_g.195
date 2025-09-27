s=input()
p=[]
for i in s:
    p.append(int(i))
for i in range(len(p)):
    p[i]=p[i]**2
for i in range(len(p)):
    p[i]=str(p[i])
print(''.join(p))

