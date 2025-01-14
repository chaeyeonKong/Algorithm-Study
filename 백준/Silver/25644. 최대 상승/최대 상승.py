import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))

minValue = arr[0]
ans=0

for i in range(1,n):
    ans = max(ans, arr[i] - minValue)
    minValue = min(minValue, arr[i])

print(ans)