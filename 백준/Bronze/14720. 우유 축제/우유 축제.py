import sys
N = int(sys.stdin.readline()[:-1])
arr = list(map(int,input().split()))
count = 0
for i in range(N):
    if arr[i] == count % 3:
        count += 1
print(count)