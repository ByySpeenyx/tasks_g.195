n=int(input())
a=[0]*(n+1)
for i in range(len(a)-1):
    a[i]=int(input())
b=[0]*len(a)# количество мест [гость, гость, ....., гость]
for i in a:
    b[i]=a.index(i)+1
b=b[1:]
for i in range(len(b)):
    b[i]=str(b[i])
print(' '.join(b))
