import sys

n = int(sys.stdin.readline().strip())
k = 1000000009
maxx = 100001
# maxx = 10
dp=[[0 for _ in range(4)] for _ in range(maxx)]

dp[1][1]=1
dp[2][2]=1
dp[3][3]=1
dp[3][1]=1
dp[3][2]=1


for i in range(4,maxx):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3])%k
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3])%k
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2])%k

for _ in range(n):
    tc = int(sys.stdin.readline().strip())
    print(((dp[tc][1] + dp[tc][2])%k + dp[tc][3])%k)
