import sys
import heapq

n = int(sys.stdin.readline().strip())
q = []

for _ in range(n):
    k = int(sys.stdin.readline().strip())
    if k==0:
        if q==[]:
            print(0)
        else:
            print(heapq.heappop(q)*-1)
    else:
        heapq.heappush(q,-k)