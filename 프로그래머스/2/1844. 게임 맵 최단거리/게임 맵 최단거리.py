from collections import deque

def solution(maps):
    check = False
    n = len(maps)
    m = len(maps[0])
    
    move=[[0,-1],[0,1],[1,0],[-1,0]] #좌우상하
    visited=[[False]*m for _ in range(n)]
    q = deque([[0,0]])
    
    while(q):
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            check = True
        visited[x][y]=True
        for i in range(4):
            idx = x+move[i][0]
            idy = y+move[i][1]
            if 0 <= idx < n and 0 <= idy<m:
                if visited[idx][idy] == False and maps[idx][idy]==1:
                    maps[idx][idy] = maps[x][y]+1
                    q.append([idx,idy])
            
    if check:
        return maps[n-1][m-1]
    else:
        return -1