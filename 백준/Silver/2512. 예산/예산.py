import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
total = int(sys.stdin.readline().strip())

start = 1
end = max(arr)
ret = 0

while(start <= end):
    t = 0
    mid = (start + end) // 2
    for i in range(0,n):
        if arr[i]>mid:
            t+=mid
        else:
            t+=arr[i]
    if t <= total:
        ret = mid
        start = mid+1
    else:
        end = mid-1

print(ret)
