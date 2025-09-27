d={}
for s in open('iban_lenght.txt'):
    s=s.split()
    print(s)
    d.update({s[0]:s[1]})
print(d)

    

