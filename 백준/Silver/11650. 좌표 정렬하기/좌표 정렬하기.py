import sys
input = sys.stdin.readline
N = int(input())
arr=[0]*N
for i in range(N):
    arr[i] = list(map(int,input().split()))
arr=sorted(arr)

for i in range(N):
    print('%d %d'%(arr[i][0],arr[i][1]))