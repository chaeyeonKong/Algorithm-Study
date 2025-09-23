import sys
a, b = map(int, sys.stdin.readline().split())

arr = []
for _ in range(a):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key = lambda x:(-x[1],-x[2],-x[3]))

for i in range(a):
    if arr[i][0]==b:
        idx = i
for i in range(a):
    if arr[idx][1:] == arr[i][1:]:
        print(i+1)
        break

