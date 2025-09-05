import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

ans = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i]==cnt and ans[j]==0:
            ans[j] = i+1
            break
        elif ans[j]==0:
            cnt+=1

for el in ans:
    print(el, end=" ")