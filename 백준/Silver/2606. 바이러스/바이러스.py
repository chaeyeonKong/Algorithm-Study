import sys
a = int(sys.stdin.readline()[:-1])
b = int(sys.stdin.readline()[:-1])
graph = [[] for _ in range(a+1)]

for i in range(b):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False] * (a+1)
count = -1

def DFS(v):
    visited[v]=True
    global count
    count+=1
    for i in graph[v]:
        if not visited[i]:
            DFS(i)
DFS(1)
print(count)