import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX = 10**5
visited=[0]*(MAX+1)

q = deque()
q.append(n)


while(q):
    cur = q.popleft()
    if cur==k:
        print(visited[cur])
        break

    for i in (cur-1, cur+1, cur*2):
        if 0<= i <=MAX and not visited[i]:
            visited[i] = visited[cur]+1
            q.append(i)