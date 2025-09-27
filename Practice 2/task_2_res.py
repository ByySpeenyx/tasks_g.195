colors={
    'bk':'0',
    'br':'1',
    'rd':'2',
    'or':'3',
    'yl':'4',
    'gr':'5',
    'bl':'6',
    'vi':'7',
    'gy':'8',
    'wh':'9',
    'au':'au',
    'ag':'ag',
    ' ':' '}
mn={
    '0':1,
    '1':10,
    '2':10**2,
    '3':10**2,
    '4':10**4,
    '5':10**5,
    '6':10**6,
    '7':10**7,
    '8':10**8,
    '9':10**9,
    ' ':' ',
    'au':'au',
    'ag':'ag'}
otkl={
    '0':' ',
    '1':1,
    '2':2,
    '3':' ',
    '4':5,
    '5':0.5,
    '6':0.25,
    '7':0.1,
    '8':0.05,
    '9':' ',
    'au':5,
    'ag':10,
    ' ':20}

def func(r):
    for i in range(len(r)):
        r[i]=colors[r[i]]
    num=int(r[0]+r[1])
    k=mn[r[2]]
    return (num*k, otkl[r[3]])
try:
    r=[input() for i in range(4)]
    print(func(r))
except KeyError:
    print(f'Unidentified or invalid band colour in bands:{r}')
    print(None, None)
