import sys

n, m = map(int, sys.stdin.readline().split())
up = [i for i in range(n + 1)]

def find(a):
    if a == up[a]:
        return a
    return find(up[a])

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        up[a] = b
    else:
        up[b] = a

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

for i in range(1, n + 1):
    up[i] = find(i)

print(len(set(up[1:])))