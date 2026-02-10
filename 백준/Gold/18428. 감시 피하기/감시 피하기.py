import sys
n = int(sys.stdin.readline().strip())
arr = []
teacher = []


def backtraking(cnt):
    global flag

    if cnt==3:
        if bfs():
            flag = True
            return
    else:
        for x in range(n):
            for y in range(n):
                if arr[x][y] == 'X':
                    arr[x][y] = 'O'
                    backtraking(cnt+1)
                    arr[x][y] = 'X'



def bfs(): # 이건 장애물을 배치했을 때 감시하는 것
    move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    for tx, ty in teacher: # 선생님의 위치에서
        for k in range(4): # 상하좌우 탐색
            xx = tx
            yy = ty

            while 0 <= xx < n and 0 <= yy < n:
                if arr[xx][yy]=='O':
                    break
                if arr[xx][yy]=='S': # 학생이 보이면 탈락!
                    return False

                xx += move[k][0]
                yy += move[k][1]

    return True




for i in range(n):
    arr.append(list(map(str, sys.stdin.readline().split())))

    for j in range(n):
        if arr[i][j]=='T':
            teacher.append([i,j])

flag = False
backtraking(0)

if flag:
    print("YES")
else:
    print("NO")