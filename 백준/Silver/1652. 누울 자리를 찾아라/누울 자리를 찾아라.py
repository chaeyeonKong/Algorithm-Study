import sys

n = int(sys.stdin.readline().strip())
# 가로
arr = []
h = 0
v = 0
for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))
    cnt = 0
    ret=[]
    for j in range(n):
        if arr[i][j]=='.':
            cnt+=1
        else:
            if cnt >= 2:
                h += 1
            cnt=0
    if cnt >= 2:
        h += 1

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[j][i] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                v += 1
            cnt = 0
    if cnt >= 2:
        v += 1
print(h, v)