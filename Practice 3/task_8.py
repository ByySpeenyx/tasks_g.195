def r(n,m):
    return min(n,m)
def k(n,m):
    return (m*n)//2
def Q(m,n):
    return min(m,n)
def K(m,n):
    return 0.5*m*n
t=int(input())
for _ in range(t):
    s=input()
    n=int(input())
    m=int(input())
    if s=='r':
        print(r(m,n))
    elif s=='k':
        print(k(m,n))
    elif s=='Q':
        print(Q(m,n))
    elif s=='K':
        print(K(m,n))
