import sys
from collections import deque

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

visited = [False for _ in range(n)]

idx = 0
cnt = 0
ret = []
while(True):

    visited[idx] = True

    if idx>=0:
        ret.append(idx+1)
    else:
        ret.append(idx+1+n)
        idx = idx+n

    lim = arr[idx]
    cnt+=1

    if arr[idx] < 0: k = -1
    else: k = 1
    move = 0
    if cnt==n:break

    while(True):
        idx+=k
        if idx>=n:
            idx = 0
        elif (idx*-1) > n:
            idx = n-1
        if visited[idx]==False:
            move+=k
        if move==lim:
            break

print(*ret)