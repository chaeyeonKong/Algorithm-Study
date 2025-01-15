import sys

n = int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().split()))
ret = 0
arr.sort()

for i in range(n+1):
    for j in range(i):
        ret+= arr[j]
print(ret)