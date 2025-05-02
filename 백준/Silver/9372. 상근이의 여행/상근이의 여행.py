import sys
k = int(sys.stdin.readline().strip())
def dfs(node, cnt):
    check[node] = 1
    for n in graph[node]:
        if check[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt


for i in range(k):
    arr = []
    cnt = 0
    n,m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]

    for j in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
        # 1. graph에 모두 연결

    check = [0] * (n+1)
    cnt = dfs(1,0)
    print(cnt)
