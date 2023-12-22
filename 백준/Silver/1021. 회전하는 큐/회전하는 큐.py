import sys
from collections import deque

qsize, num = map(int,sys.stdin.readline().split())
arr = deque([i for i in range(1,qsize+1)])
count = 0
li = list(map(int,sys.stdin.readline().split()))

for idx in range(len(li)):
        target = li[idx]
        while True:
            if target == arr[0]:
                arr.popleft()
                break
            else:
                if arr.index(target) < len(arr)/2:
                    arr.rotate(-1)
                else:
                    arr.rotate(1)
                count+=1
print(count)