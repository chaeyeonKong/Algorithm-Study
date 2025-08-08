# 토마토
import sys
from collections import deque

m, n= map(int, sys.stdin.readline().split())
arr = []
move = [[0,-1],[0,1],[-1,0],[1,0]]
mcount = 0
res = 0

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

q = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))

while(q):
    idx, idy = q.popleft()

    for i in range(4):
        idxx = idx + move[i][0]
        idyy = idy + move[i][1]

        if 0 <= idxx < n and 0 <= idyy < m:
            if arr[idxx][idyy] ==0: # 0보다 크거나 같은것이 아니라 0인 것을 찾아야함
                arr[idxx][idyy] = arr[idx][idy]+1 # 배열 자체에 depth를 넣어줌
                q.append((idxx,idyy))

for i in arr:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res-1)
