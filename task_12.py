from math import*
def kilotobait(x):
    x*=1024
    return x
def baittokilo(x):
    x/=1024
    return ceil(x)
print('what u wanna do: 1 - килобайты -> байты ; 2 - байты -> килобайты.')
a=int(input())
if a==1:
    print("skol'ko kilobaitov???")
    k=int(input())
    print(kilotobait(k))
elif a==2:
    print("skol'ko baitov???")
    b=int(input())
    print(baittokilo(b))
else:
    print('u can choose only beetween 1 and 2')
