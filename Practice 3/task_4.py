def linsech(arr, tar):
    if len(arr)==0:
        return -1
    if len(arr)==1 and arr[0]==tar:
        return a[0]
    for i in range(len(arr)):
        if arr[i]==tar:
            return i
n=int(input())
arr=[int(input()) for i in range(n)]
tar=int(input())
print(linsech(arr, tar))
