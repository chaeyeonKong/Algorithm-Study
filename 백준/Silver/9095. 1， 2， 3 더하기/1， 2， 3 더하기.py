import sys
n = int(sys.stdin.readline().strip())
dp = [0,1,2,4,7,0,0,0,0,0,0,0]
for _ in range(n):
    k = int(sys.stdin.readline().strip())
    for i in range(5,k+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[k])