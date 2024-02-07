import sys
n = int(sys.stdin.readline().strip())
arr=[0]*10001

for i in range(n):
    k = int(sys.stdin.readline().strip())
    arr[k] += 1 #count 정렬을 위한

for i in range(10001):
    if arr[i] !=0:
        for j in range(arr[i]):
            print(i)