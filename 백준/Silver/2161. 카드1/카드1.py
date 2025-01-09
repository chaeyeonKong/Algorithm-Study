import sys
from collections import deque

n = int(sys.stdin.readline().strip())
ret=[]
arr = deque()

for i in range(n):
    arr.append(i+1)

while(arr):
    target = arr[0]
    ret.append(target)
    arr.popleft()
    if arr:
        target = arr[0]
        arr.append(target)
        arr.popleft()
print(*ret)

