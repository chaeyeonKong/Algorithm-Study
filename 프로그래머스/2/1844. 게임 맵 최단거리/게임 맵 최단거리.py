from collections import deque
def solution(maps):
    
    q = deque([[0,0]])
    
    n = len(maps)
    m = len(maps[0])
    
    visited=[[False] * m for _ in range(n)]
    arr = [[0] * m for _ in range(n)]
    visited[0][0]=[True]
    
    cnt = 0
    
    move=[[0,-1],[0,1],[1,0],[-1,0]]
    
    while(q):
        cnt+=1
        i, j = q.popleft()
        for x, y in move:
            x += i
            y += j
            if 0<=x<n and 0<=y<m: #범위 안에서
                if visited[x][y] == False: #방문하지 않았다면
                    if maps[x][y]==1: # 갈 수 있다면
                        arr[x][y] = arr[i][j]+1
                        visited[x][y] = True
                        q.append([x,y])
    if arr[n-1][m-1]==0:
        return -1
    else:
        return arr[n-1][m-1]+1