def func(s):
    soft=[2, 3, 5, 7, 11, 13, 17]
    r=[]
    if s[0]!='0':
        for i in range(1,len(s)-2):
            b=int(s[i:i+3])
            for j in soft:
                if b%j==0:
                    r.append(b)
    return sum(r)
s='1406357289'
print(func(s))

