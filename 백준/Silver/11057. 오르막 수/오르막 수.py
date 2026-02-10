import sys
n = int(sys.stdin.readline().strip())
dp=[1] *10

for i in range(1,n):
    for j in range(10):
        dp[j] = sum(dp[j:])
    # print(dp)
print(sum(dp)%10007)