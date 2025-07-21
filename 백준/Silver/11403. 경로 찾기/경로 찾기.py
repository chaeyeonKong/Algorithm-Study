## 방향이 있는 그래프
import sys
from collections import deque

arr = []
n = int(sys.stdin.readline().strip())
visited= [[0 for _ in range(n)] for _ in range(n)]
node = deque()
q = deque()

for i in range(n):
    li = list(map(int,sys.stdin.readline().split()))
    for j in range(len(li)):
        if li[j]==1:
            node.append([i,j])
    arr.append(li)


for el in node:
    q.append(el)
    fixx = el[0]
    while(q):
        x,y = q.popleft()
        visited[x][y] = 1
        for nd in node:
            if nd[0] == y:
                if visited[fixx][nd[1]] == 0:
                    visited[fixx][nd[1]]=1
                    q.append(nd)

for i in range(n):
    for j in range(n):
        print(visited[i][j],end=" ")
    print()
