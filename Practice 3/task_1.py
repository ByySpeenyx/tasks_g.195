def func(s1, s2):
    b=True
    for i in s1:
        if i not in s2:
            b=False
    if b==True and len(s1)==len(s2):
        return "they're annogramms"
    else:
        return "they're not annogramms "
s1=input()
s2=input()
print(func(s1,s2))
