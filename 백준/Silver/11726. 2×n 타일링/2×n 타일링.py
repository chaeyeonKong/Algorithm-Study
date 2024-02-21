import sys
def fibo(k):

    if k==1:
        return 1
    elif k==2:
        return 2
    else:
        if memo[k]==0:
            memo[k] = fibo(k - 1) + fibo(k - 2)
        return memo[k]

k = int(sys.stdin.readline().strip())
memo = [0]*(k+1)
ans = fibo(k)
print(ans%10007)