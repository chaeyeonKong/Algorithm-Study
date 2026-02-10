import sys
n = int(sys.stdin.readline().strip())

arr = []
teacher = []
flag = False



def backtraking(cnt):
    global flag

    if cnt == 3:
        if bfs():
            flag = True
        return

    for i in range(n):
        for j in range(n):
            if arr[i][j]=='X':
                arr[i][j]='O'
                backtraking(cnt+1)
                arr[i][j]='X'

def bfs():
    move=[[-1,0],[1,0],[0,1],[0,-1]]
    for tx, ty in teacher:
        for i in range(4):
            nx = tx
            ny = ty
            while(True):
                nx += move[i][0]
                ny += move[i][1]

                if 0 <= nx < n and 0 <= ny < n:

                    if arr[nx][ny]=='O':
                        break
                    if arr[nx][ny]=='S':
                        return False
                else:
                    break
    return True

for i in range(n):
    arr.append(list(map(str, sys.stdin.readline().split())))
    for j in range(n):
        if arr[i][j] == 'T':
            teacher.append([i,j])

backtraking(0)

if flag:
    print("YES")
else:
    print("NO")