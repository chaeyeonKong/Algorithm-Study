from collections import deque

def solution(maps):
    
    move = [(1,0),(-1,0),(0,-1),(0,1)] # 상하좌우
    
    visited=[[ False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    ret=[]
    q = deque()
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]!='X' and visited[i][j]==False:
                q.append((i,j))
                ans = int(maps[i][j])
                visited[i][j]=True
                while(q):
                    x, y = q.popleft()
                    
                    for k in range(4):
                        xx = x+int(move[k][0])
                        yy = y+int(move[k][1])
                    
                        if 0<=xx<len(maps) and 0<=yy<len(maps[0]):
                            if visited[xx][yy]==False: #방문하지 않았다면
                                visited[xx][yy]=True
                                if maps[xx][yy]!='X':
                                    q.append((xx,yy))
                                    ans+= int(maps[xx][yy])
                ret.append(ans)

    if ret==[]:
        ret = [-1]
    else:
        ret.sort()

    return ret