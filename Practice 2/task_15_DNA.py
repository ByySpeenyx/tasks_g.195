s=input()
partG = int((s.count('G')/len(s)*100))
partC = int((s.count('C')/len(s)*100))
print(f' doli G i C v stroke: {partG}% i {partC}%\n')
for i in range(len(s)):
    if s[i] in 'AT':
        s=s.replace(s[i],'*')
    if s[i] in 'CG':
        s=s.replace(s[i],'%')
if s==s[::-1]:
    print('stroka - palindrom)))')
else:
    print('stroka ne palindrom(((')
