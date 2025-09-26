import sys
n =int(sys.stdin.readline().strip())
arr = []
heart = []

for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))

head = False
for i in range(n):
    for j in range(n):
        if arr[i][j] == '*':
            if head==False:
                heart = [i+1, j]
                head = True
                break

move=[[0, -1],[0,1],[1,0],[1,0],[1,0]]
print(heart[0]+1, heart[1]+1)


ret = []
for i in range(5):
    if i==3:
        heart = [x - 1, y - 1]
    if i==4:
        heart[1] +=2

    x, y = heart[0], heart[1]  # 심장위치
    cnt = 0
    while(True):
        x += move[i][0]
        y += move[i][1]
        if 0<=x<n and 0<=y<n:
            if arr[x][y] == '*':
                cnt+=1
            else:
                break
        else:
            break
    ret.append(cnt)

print(*ret)
