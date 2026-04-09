import sys
n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))
arr = sorted(arr)

start = 0; end = 1

ans = 2000000001
while(end<n):
    k = abs(arr[end] - arr[start])


    if k<m:
        end+=1
    elif k>m:
        start+=1
        if k < ans:  # 차이가 최소이면
            ans = k
    elif m==k:
        ans = m
        break
    if start == end:
        end = start+1
print(ans)