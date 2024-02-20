import sys
k = int(sys.stdin.readline().strip())
for _ in range(k):
    n = int(sys.stdin.readline().strip())
    dp=[1,2,4,0,0,0,0,0,0,0,0]

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    print(dp[n-1])