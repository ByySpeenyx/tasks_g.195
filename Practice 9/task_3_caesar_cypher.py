from string import ascii_lowercase
def crypto(s, m):
    alp=ascii_lowercase
    r=""
    for i in s:
        if  i==" " or i=="!" or i==",":
            r+=i
            continue
        if i in alp.upper():
            r+=alp[(alp.index(i.lower())+m)%26].upper()
        else:
             r+=alp[(alp.index(i)+m)%26]
    return r

def caesar_cipher(s, m, mode="encrypt"):
    if mode=="encrypt":
        return crypto(s,m)
    else:
        m=-m
        return crypto(s, m)
    
print(caesar_cipher("Hello", 3, 'encrypt'))          # Должно вернуть: "Khoor"
print(caesar_cipher("Khoor", 3, 'decrypt'))          # Должно вернуть: "Hello"
print(caesar_cipher("XYZ", 5, 'encrypt'))            # Должно вернуть: "CDE" (циклический сдвиг)
print(caesar_cipher("Hello, World!", 13, 'encrypt')) # Должно вернуть: "Uryyb, Jbeyq!"
