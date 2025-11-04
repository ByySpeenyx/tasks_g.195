def func(arr):
    mx=max(arr)
    mn=min(arr)
    return (arr.index(mn)+1, arr.index(mx)+1)
print(func([100, 120, 140, 160, 180, 200, 220]))
print(func([200, 180, 220, 160, 240, 260, 210]))
print(func([250, 230, 210, 190, 170, 150, 130]))
print(func([200, 200, 200, 200, 200, 200, 200]))
print(func([150, 160, 155, 170, 180, 175, 165]))
