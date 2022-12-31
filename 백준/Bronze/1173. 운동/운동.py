import sys
input = sys.stdin.readline
N,m,M,T,R = map(int,input().split())
fix_m=m; ex = 0;i=0
if (m + T) > M: i = -1
else:
    while(ex<N):
        i+=1
        if m+T<=M:
            m+=T; ex+=1
        else: m-=R
        if m < fix_m: m = fix_m
print(i)