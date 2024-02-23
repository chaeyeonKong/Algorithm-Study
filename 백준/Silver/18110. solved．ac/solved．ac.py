import sys
from collections import deque

def round_(num):
    if (num-int(num)) >= 0.5:
        return int(num)+1
    else:
        return int(num)

q = deque()
n =int(sys.stdin.readline().strip())

for i in range(n):
    q.append(int(sys.stdin.readline().strip()))
q = deque(sorted(q))

k = round_(n*(15/100))

for _ in range(k):
    q.pop()
    q.popleft()

if sum(q)<=0:
    print(0)
else:
    print(round_(sum(q)/len(q)))