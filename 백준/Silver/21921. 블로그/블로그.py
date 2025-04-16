import sys
n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

k = -1
s=0

for i in range(n):
    s += arr[i]
    if i-(x-1)>0:
        s-= arr[i-x]

    if s > k and s!=0:
        k = s
        cnt = 1
    elif s==k:
        cnt+=1

if k==-1:
    print("SAD")
else:
    print(k)
    print(cnt)