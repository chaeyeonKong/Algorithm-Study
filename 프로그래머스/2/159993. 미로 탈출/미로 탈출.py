from collections import deque

def solution(maps):
    
    move = [[0,-1],[0,1], [1,0], [-1,0]] #좌우상하
    q = deque([])    
    
    n = len(maps)
    m = len(maps[0])
    k = (n*m)+1
    
    visited = [ [False for _ in range(m)] for _ in range(n) ]
    arr = [ [k for _ in range(m)]for _ in range(n) ]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]=="S":
                q.append((i,j))
                visited[i][j]=True
                arr[i][j]=0
            if maps[i][j]=="E":
                ex = i
                ey = j
            if maps[i][j]=="L":
                lx = i
                ly = j
    
    cnt=0
    while(q):
        x,y = q.popleft()
        for i in range(4):
            dx = x+move[i][0]
            dy = y+move[i][1]
            
            if 0<=dx<n and 0<=dy<m:
                if visited[dx][dy]==False:
                    visited[dx][dy]=True
                    
                    if maps[dx][dy]!="X":
                        cnt+=1
                        q.append((dx,dy))
                        arr[dx][dy] = min(arr[dx][dy],arr[x][y]+1)
                        if maps[dx][dy]=="L": 
                            q = deque([])
                            break
    
    if arr[lx][ly]==k:
        return -1
    
    to_lv = arr[lx][ly]
    arr = [ [k for _ in range(m)]for _ in range(n) ]
    arr[lx][ly] = 0
    
    q = deque([(lx,ly)])
    
    visited = [ [False for _ in range(m)] for _ in range(n) ]
    visited[lx][ly]=True
    
    while(q):
        x,y = q.popleft()
        for i in range(4):
            dx = x+move[i][0]
            dy = y+move[i][1]

            if 0<=dx<n and 0<=dy<m:
                if visited[dx][dy]==False:

                    if maps[dx][dy]!="X":
                        visited[dx][dy]=True
                        cnt+=1
                        q.append((dx,dy))
                        arr[dx][dy] = min(arr[dx][dy],arr[x][y]+1)
                        
    if arr[ex][ey]==k:
        return -1
    else:
        return to_lv + arr[ex][ey]
    