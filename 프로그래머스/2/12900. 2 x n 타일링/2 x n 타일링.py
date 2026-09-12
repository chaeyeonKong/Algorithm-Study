def solution(n):
    # n=1000
    if n<=3:
        return n
    
    dp = [0 for _ in range(n+1)]
    for i in range(4):
        dp[i] = i
        
    a = dp[2]
    b = dp[3]
    for i in range(4,n+1):
        dp[i] = (a + b)%1000000007
        a = dp[i-1]
        b = dp[i]
        
    # print(dp)
    ans = dp[-1]
    return ans