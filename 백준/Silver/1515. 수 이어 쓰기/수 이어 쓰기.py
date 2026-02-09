import sys
from collections import deque

n = str(sys.stdin.readline().strip()) # queue를 써볼까
queue = deque(list(str(n)))

su = 0
while(queue):
    su += 1
    k = deque(list(str(su)))
    while(queue and k):
        el = k.popleft()
        if queue[0]==el:
            queue.popleft()


print(su)


