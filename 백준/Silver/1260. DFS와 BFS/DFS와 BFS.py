import sys
from collections import deque

node, line, root = map(int,sys.stdin.readline().split())

graph = [[0]*(node+1) for _ in range(node+1)]
for i in range(line):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a]=1

visited1=[0]*(node+1)
visited2 = visited1.copy()


def dfs(x):
    visited2[x] = 1
    print(x, end= ' ')
    for i in range(1,node+1):
        if (visited2[i] == 0 and graph[x][i]==1):
            dfs(i)


def bfs(x):
    visited1[x] = 1
    queue = [x]
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1,node+1):
            if (visited1[i]==0 and graph[v][i]==1):
                queue.append(i)
                visited1[i] = 1


dfs(root)
print()
bfs(root)

