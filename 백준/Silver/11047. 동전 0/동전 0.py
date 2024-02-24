import sys
n, k = map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))
arr = arr[::-1]
count=0
for i in range(n):
    count += k//arr[i]
    k = k%arr[i]
print(count)