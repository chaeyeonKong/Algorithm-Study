import sys

a,b = map(int,sys.stdin.readline().split())
arr=[]
for _ in range(a):
    arr.append(int(sys.stdin.readline().strip()))

start = 1; end = max(arr)

while(start<=end):
    mid = (start+end)//2

    lines=0
    for el in arr:
        lines += el//mid

    if lines>=b:
        start=mid+1
    else:
        end = mid-1

print(end)