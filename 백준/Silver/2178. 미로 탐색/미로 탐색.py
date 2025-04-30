import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

arr = []
move = [[0,1],[1,0],[-1,0],[0,-1]]

for i in range(n):
    arr.append(list((map(int,' '.join(sys.stdin.readline().split())))))

queue = deque([(0,0)])

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nextx = x + move[i][0]
        nexty = y + move[i][1]

        if 0<=nextx <n and 0<=nexty<m:
            if arr[nextx][nexty]==1:
                queue.append((nextx, nexty))
                arr[nextx][nexty] = arr[x][y] +1

print(arr[n-1][m-1])