import sys
input = sys.stdin.readline

d=[0]*100
a = int(input()[:-1])

def fibo(x):
    if d[x] == 0:
        if x==0: return 0
        if x==1: return 1
        d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(a))