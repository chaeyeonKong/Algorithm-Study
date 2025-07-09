import sys
from collections import deque

n = int(sys.stdin.readline().strip())

arr = []

move = [[0,1],[0,-1],[1,0],[-1,0]]
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]


for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip())))
ret_cnt = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1: #방문하지 않았다면
            q.append([i,j])
            cnt = 1
            while(q):
                x, y = q.pop()
                visited[x][y] = True
                for l in range(4):
                    idxx = x+move[l][0]
                    idyy = y+move[l][1]
                    if 0 <= idxx < n and 0 <= idyy < n:
                        if arr[idxx][idyy] == 1 and not visited[idxx][idyy]:
                            cnt += 1
                            q.append([idxx,idyy])
                            visited[idxx][idyy] = True
            ret_cnt.append(cnt)

ret_cnt.sort()

print(len(ret_cnt))
for el in ret_cnt:
    print(el)