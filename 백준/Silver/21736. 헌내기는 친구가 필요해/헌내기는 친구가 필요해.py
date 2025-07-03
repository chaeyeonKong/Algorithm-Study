import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

arr = []
move = [[0,-1],[0,1],[1,0],[-1,0]]
for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))

q = deque()
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j]=='I':
            q.append([i,j])

while (q):
    i, j = q.pop()
    visited[i][j] = True

    for mx, my in move:
        idx = i+mx
        idy = j+my
        if 0 <= idx < n and 0<= idy < m:

            if not visited[idx][idy] and arr[idx][idy] != 'X':
                visited[idx][idy] = True
                if arr[idx][idy] == 'P':
                    cnt += 1
                q.append((idx, idy))     

if cnt>0:
    print(cnt)
else:
    print("TT")