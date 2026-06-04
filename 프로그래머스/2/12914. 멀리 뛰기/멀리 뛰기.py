def solution(n):
    dp = [ i for i in range(n+1)]
    if n<=3:
        return dp[n]%1234567 
    for i in range(3, n+1):
        dp[i] = dp[i-2]+dp[i-1]
    return dp[n]%1234567