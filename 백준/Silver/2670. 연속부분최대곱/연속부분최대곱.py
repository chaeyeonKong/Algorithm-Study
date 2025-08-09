import sys

n = int(sys.stdin.readline().strip())
arr = []
dp=[0.0 for _ in range(n)]

for _ in range(n):
    arr.append(float(sys.stdin.readline().strip()))

dp[0] = arr[0]
ans = arr[0]

if n>1:
    for i in range(1,n):
        dp[i] = max(arr[i],dp[i-1]*arr[i])
        ans = max(ans, dp[i])

print("%.3f"%ans)
