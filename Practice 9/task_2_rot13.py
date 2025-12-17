from string import*
def encrypter(s):
    r=""
    alp=ascii_lowercase
    for i in s:
        if i==" ":
            r+=i
            continue
        if i in alp.upper():
            r+=alp[(alp.index(i)+13)%len(alp)].upper()
        else:
            r+=alp[(alp.index(i)+13)%len(alp)]
    return r


s="abcd"
s1=encrypter(s)
print(s1, " ", encrypter(s1))
