import sys
input = sys.stdin.readline
N = int(input())
arr=[0]*N
current = -1
for i in range(N):
    k = int(input())

    if k == 0:
        arr[current]=0
        current-=1
    else:
        arr[current+1] = k
        current+=1

print(sum(arr))