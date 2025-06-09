import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
move = [[0,1],[0,-1],[1,0],[-1,0]] # 좌우상하 이동좌표

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

visited = [[False for _ in range(m)] for _ in range(n)]
ans = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            visited[i][j] = True
            q = deque([(i,j)]) # target의 위치 등록

while q:
    x, y = q.popleft() #타겟의 x, y 좌표
    for dx, dy in move:
        nx = x+dx
        ny = y+dy

        # 범위 내, 1이고, 방문하지 않았다면
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
            q.append((nx,ny)) # q에 넣어서 현재 위치를 업데이트 시킴
            visited[nx][ny] = True
            ans[nx][ny] = ans[x][y] + 1

for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1: # 방문하지 않았는데 1인 경우
            print(-1, end = " ")
        else:
            print(ans[i][j], end =" ")
    print()