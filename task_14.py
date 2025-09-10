dayofweek=int(input())
days=int(input())
m=[0]*7
i=1
while True:
    m[dayofweek-1]=i
    i+=1
    dayofweek+=1
    if dayofweek>7:
        for z in range(len(m)):
            m[z]=str(m[z])
            if m[z]=='0':
                m[z]='  '
            if len(m[z])<2:
                m[z]+=' '
        print(' '.join(m))
        dayofweek=1
        m=[0]*7
    if i>days:
        for z in range(len(m)):
            m[z]=str(m[z])
            if m[z]=='0':
                m[z]='  '
            if len(m[z])<2:
                m[z]+=' '
        print(' '.join(m))
        break
    






































##while days!=0:
##    m=[0]*7
##    m[dayofweek]=i
##    i+=1
##    dayofweek+=1
##    days-=1
##    if dayofweek==7:
##        print(m)
##        m=[0]*7
    
    
