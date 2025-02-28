import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[] for _ in range (n)]
dp[0] = arr[0]

for i in range(1,n):
    dp[i] = dp[i-1]+arr[i]


for i in range(m):
    ii, jj = map(int, sys.stdin.readline().split())
    if ii>1:
        print(dp[jj-1] - dp[ii-2])
    else:
        print(dp[jj-1])

