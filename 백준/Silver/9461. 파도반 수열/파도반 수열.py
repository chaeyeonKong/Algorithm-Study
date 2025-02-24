arr = [1,1,1,2,2,3,4]

import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    a = int(sys.stdin.readline().strip())
    a-=1
    if a <= len(arr)-1:
        print(arr[a])
    else:
        while(len(arr)-1!=a):
            idx = len(arr)-1
            arr.append(arr[idx-2] + arr[idx-1])
        print(arr[a])