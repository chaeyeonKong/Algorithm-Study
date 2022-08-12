import sys
input = sys.stdin.readline
N = int(input())
arr=[0]*N
for i in range(N):
    arr[i] = list(map(int,input().split()))
arr = sorted(arr,key=lambda x:(x[1],x[0]))

for i in range(N):
    print('%d %d'%(arr[i][0],arr[i][1]))