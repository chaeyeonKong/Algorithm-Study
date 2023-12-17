import sys
sys.setrecursionlimit(10**6)  # 재귀 제한 늘림
n,m = map(int, sys.stdin.readline().split())

arr=[[]for _ in range(n+1)]
visited=[False]*(n+1)
count=0

def dfs(node):
    visited[node] = True
    for next in arr[node]:
        if not visited[next]:
            dfs(next)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

for node in range(1,n+1):

    if not visited[node]:
        dfs(node)
        count+=1

print(count)