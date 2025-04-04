import sys
n = int(sys.stdin.readline().strip())
arr = []

for i in range(n):
    arr.append(str(sys.stdin.readline().strip()))

idx = (len(arr[0]))-1
while(True):
    arr2 = []
    for i in range(n):
        if arr[i][idx:len(arr[0])] not in arr2:
            arr2.append(arr[i][idx:len(arr[0])])
        else:
            continue
    if len(arr2)==n:break
    idx-=1

print(len(arr[0])-idx)
