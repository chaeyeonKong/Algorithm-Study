import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())
visited = [[[False]*m for _ in range(n)]for _ in range(h)]
arr = []
queue = deque()

for k in range(h):
    temp = []
    for i in range(n):
        li = list(map(int, sys.stdin.readline().split()))
        for j in range(len(li)):
            if li[j]==1:
                queue.append([k,i,j]) # 차원, x, y
        temp.append(li)
    arr.append(temp)
# 토마토 배열 완성

move = [(0,-1,0),(0,1,0),(0,0,1),(0,0,-1),(1,0,0),(-1,0,0)] #차원 동일(왼, 오, 위, 아래, / 차원이동 앞, 뒤)
# cmove = []

ret = 0

while(queue): # target 대상으로 bfs 진행
    k,x,y = queue.popleft() # popleft가 핵심
    # move가 범위 내인가?
    for a,b,c in move:
        if 0<=k+a<h and 0<=x+b<n and 0<=y+c<m:
            kk = k+a
            xx = x+b
            yy = y+c
            # 여기서 비교는 무조건 0일때만
            if arr[kk][xx][yy]==0:
                queue.append([kk, xx, yy])
                arr[kk][xx][yy]=arr[k][x][y]+1

zero_check = False
def answer(arr):
    ret = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j] == 0:
                    return -1
                ret = max(ret, arr[k][i][j])
    if ret > 0:
        ret -= 1
    return ret

print(answer(arr))

