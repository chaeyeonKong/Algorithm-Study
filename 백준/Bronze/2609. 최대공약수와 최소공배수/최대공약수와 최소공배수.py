import sys
n,m = map(int,sys.stdin.readline().split())
ran = max(n,m)
so=1; dae=1; k = 2

while(True):
    if ran < k:
        so = dae * n * m
        print(dae, so)
        break

    if n%k==0 and m%k==0:
        dae *= k
        n//=k
        m//=k
    else:
        k+=1