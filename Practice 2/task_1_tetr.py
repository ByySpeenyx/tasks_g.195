def tetration(grade, number):
    num=1
    for i in range(grade):
        num*=number
    return number**num
check1=str(tetration(3,5))
check2=str(tetration(5,2))
print(len(check1), len(check2))
