import sys
n = int(sys.stdin.readline().strip())
dp = [0,1,3,5]

for i in range(4, n+1):
    dp.append((dp[i-1] + (dp[i-2]*2)))

print(dp[n]%10007)