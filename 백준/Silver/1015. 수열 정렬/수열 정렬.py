import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
b = sorted(a)
ret = []
visited = [False for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i]==b[j]:
            if visited[j]==False:
                visited[j]=True
                ret.append(j)
                break
print(*ret)