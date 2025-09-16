def accum(s):
    p=[]
    for i in s:
        if 65<=ord(i)<=90:
            p.append(i+chr(ord(i)+32)*s.index(i))
        else:
            p.append(chr(ord(i)-32)+i*s.index(i))
    return p
s=input()
s=accum(s)
print("-".join(s))
