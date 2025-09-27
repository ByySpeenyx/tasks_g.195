s=input()
s=s.split()
north=[]
south=[]
west=[]
east=[]
r=[]
for i in s:
    if i=='NORTH':
        north.append(i)
    if i=='SOUTH':
        south.append(i)
    if i=='WEST':
        west.append(i)
    if i=='EAST':
        east.append(i)
if len(north)- len(south)>0:
    for i in range(len(north)-len(south)):
        r.append('NORTH')
else:
    for i in range(len(south)-len(north)):
        r.append('SOUTH')
if len(west)-len(east)>0:
    for i in range(len(west)-len(east)):
        r.append('WEST')
else:
    for i in range(len(east)-len(west)):
        r.append('EAST')
print(r)
