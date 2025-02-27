import sys
import heapq

n = int(sys.stdin.readline().strip())
q = []
for _ in range(n):
    k = int(sys.stdin.readline().strip())
    if k==0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,k)