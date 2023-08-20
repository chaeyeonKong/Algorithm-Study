import sys
arr=[]
for i in range(4):
    a, b = map(int, sys.stdin.readline()[:-1].split())
    if i==0:
        arr.append(b-a)
    else:
        arr.append(arr[len(arr)-1]+(b-a))
print(max(arr))