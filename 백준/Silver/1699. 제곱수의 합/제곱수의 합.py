import sys

k = int(sys.stdin.readline().strip())
dp = [i for i in range(k+1)]

for i in range(2,k+1):
    for j in range(1,i+1):
        sqrt_ = j*j
        if sqrt_ > i:
            break
        if dp[i]>dp[i-sqrt_]+1:
            dp[i] = dp[i - sqrt_] + 1
print(dp[k])