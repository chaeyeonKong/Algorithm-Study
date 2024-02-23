import sys
from collections import deque

k = int(sys.stdin.readline().strip())

for _ in range(k):
    n,m = map(int,sys.stdin.readline().split())
    s = list(map(int,(sys.stdin.readline().split())))

    q = deque()

    for i,x in enumerate(s):
        q.append((i,x))

    s.sort()
    count=0
    while(q):
        i,x = q.popleft()
        if x==s[-1]:
            s.pop()
            count+=1
            if i==m:
                print(count)
                break
        else:
            q.append((i,x))