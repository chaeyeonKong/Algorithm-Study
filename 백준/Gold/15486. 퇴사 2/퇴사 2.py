import sys
n = int(sys.stdin.readline().strip())
time = [0]
price = [0]
dp = [0 for _ in range(n+1)]

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    time.append(a)
    price.append(b)

for i in range(1,n+1):
    dp[i] = max(dp[i], dp[i-1])
    fin_date = i + time[i] - 1
    if fin_date <= n :
        dp[fin_date] = max(dp[fin_date],dp[i-1]+price[i])

print(max(dp))
