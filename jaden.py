from string import ascii_lowercase
alp=ascii_lowercase
s=input()
p=[]
for i in s:
    p.append(i)
for i in range(len(p)-1):
    if p[i]==' ' and p[i+1] in alp:
        p[i+1]=chr(ord(p[i+1])-32)
print(''.join(p))
        
