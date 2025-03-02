import sys

n,m = map(int, sys.stdin.readline().split())

s  = []
ret = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str,s)))

    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)