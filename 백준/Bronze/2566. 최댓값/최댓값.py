import sys
arr = []
for i in range(9):
    arr.append(list(map(int, sys.stdin.readline().split())))

k = arr[0][0]
idx1 = 0
idx2 = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > k:
            k = arr[i][j]
            idx1 = i
            idx2 = j
print(k)
print(idx1+1, idx2+1)