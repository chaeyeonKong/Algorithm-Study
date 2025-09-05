import sys
n,k =  map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline().strip()))

dp = [10001 for _ in range(k+1)]
dp[0] = 0

for i in range(k+1):
    for el in coin:
        if i<el:
            continue
        dp[i] = min(dp[i], dp[i-el]+1)

if dp[-1]==10001:
    print(-1)
else:
    print(dp[-1])