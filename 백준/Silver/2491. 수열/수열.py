import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
dp=[0 for _ in range(n)]
dp[0] = 1
dp2=[0 for _ in range(n)]
dp2[0] = 1


for i in range(1,n):
    if arr[i-1]<=arr[i]:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = 1

    if arr[i] <= arr[i-1]:
        dp2[i] = dp2[i-1]+1
    else:
        dp2[i] = 1

print(max(max(dp2),max(dp)))
