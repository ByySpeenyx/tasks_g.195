def tetration(grade, number):
    num=1
    for i in range(grade):
        num*=number
    return number**num
n=int(input())
k=int(input())
print(len(str(tetration(n,k))))

