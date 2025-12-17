def get_dih(d, key, value):
    d[key]=value
    d[value]=key
    d[key.upper()]=value.upper()
    d[value.upper()]=key.upper()

def get_key_value(s):
    d={}
    m=[]
    for i in range(2, len(s), 2):
        m.append(s[i-2: i])
    for i in m:
        get_dih(d, i[0], i[1])
    return d
def encrypter(s,d):
    r=""
    for i in s:
        if i in d:
            r+=d[i]
            continue
        r+=i
    return r
def encode(message, key):
    d=get_key_value(key)
    return encrypter(message, d)
def decode(message, key):
    d=get_key_value(key)
    return encrypter(message, d)

print(encode("ABCD", "agedyropulik"))             
print(encode("Ala has a cat", "gaderypoluki"))     
print(decode("Dkucr pu yhr ykbir","politykarenu"))
print(decode("Hmdr nge brres","regulaminowy"))     
        
