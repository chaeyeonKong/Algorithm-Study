import sys
from collections import deque
n = int(sys.stdin.readline().strip())
arr = []
target = deque()

for _ in range(n):
        arr = list(map(int,sys.stdin.readline().split()))
        for j in range(n):
                if len(target)<n:
                        target.append(arr[j])
                        target = sorted(target)
                elif arr[j] > target[0]:
                    target.pop(0)
                    target.append(arr[j])
                    target = sorted(target)
print(target[0])
