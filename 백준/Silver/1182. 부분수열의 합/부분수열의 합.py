import sys
n, k = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
dp= [[] for _ in range(n)]

cnt = 0

for i in range(n):
    if arr[i]==k:
        cnt+=1
    dp[i].append(arr[i])
    for j in range(i):
        for l in range(len(dp[j])):
            if arr[i]+dp[j][l]==k:
                cnt+=1
            dp[i].append(arr[i]+dp[j][l])

print(cnt)
