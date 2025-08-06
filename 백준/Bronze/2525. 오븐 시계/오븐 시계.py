import sys

a, b = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline().strip())


target = b+k
m=0
n=0
if target>=60:
    m = target//60
    n = target%60
    a+=m
    if a>=24:
        a%=24
    print(a, n)
else:
    if a>=24:
        a%=24
    print(a, b+k)