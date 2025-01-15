import sys

n = int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().split()))

mini = arr[0]
ret = 0
for i in range(n):
    ret = max(ret, arr[i]-mini)
    mini = min(mini, arr[i])
print(ret)
