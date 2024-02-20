import sys
n = int(sys.stdin.readline().strip())
dp = [0]*(n+1)
ans = [""]*(n+1)
ans[1]="1"

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    prev = i-1

    if i%3==0 and dp[i//3]+1<dp[i]:
        dp[i] = dp[i//3]+1
        prev = i//3

    if i%2==0 and dp[i//2]+1 < dp[i]:
        dp[i] = dp[i//2]+1
        prev = i//2

    ans[i] = str(i) + " " + ans[prev]

print(dp[n])
print(ans[n])