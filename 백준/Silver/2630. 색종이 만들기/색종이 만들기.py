import sys
from collections import deque

n = int(sys.stdin.readline().strip())
arr = []

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
white = 0
blue = 0

def cut(row, column, n):
    global white, blue
    color = arr[row][column]

    for i in range(row, row+n):
        for j in range(column, column+n):
            if color != arr[i][j]:
                cut(row, column, n // 2)
                cut(row, column + n // 2, n // 2)
                cut(row + n // 2, column, n // 2)
                cut(row + n // 2, column + n // 2, n // 2)
                return

    if color==0:
        white+=1
    else:
        blue+=1

cut(0,0,n)

print(white)
print(blue)