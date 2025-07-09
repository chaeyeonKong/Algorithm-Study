import sys
from itertools import combinations

n = int(sys.stdin.readline().strip())
arr = []

for i in range(n):
    c, d = map(int, sys.stdin.readline().split())
    arr.append((c,d))

answer = abs(arr[0][0]-arr[0][1])

for i in range(1, n+1):
    cases = combinations(range(n),i)
    for case in cases:
        ret1 = 1
        ret2 = 0
        for j in range(len(arr)):
            if j in case:
                ret1 *= arr[j][0]
                ret2 += arr[j][1]
        answer = min(answer, abs(ret1-ret2))

print(answer)