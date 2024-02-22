import sys, queue
n, k = map(int,sys.stdin.readline().split())

def fact(t):
    ret = 1
    for i in range(t,1,-1):
        ret *= i
    return ret

print(fact(n)//(fact(n-k)*fact(k)))