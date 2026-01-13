# 시간초과 -> set & dict
import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
comp = sorted(set(arr))

index = dict()

for cnt, i in enumerate(comp):
    index[i] = cnt

for el in arr:
    print(index[el], end = ' ')
