import sys
n ,d = map(int, sys.stdin.readline().split())
dp = [i for i in range(0,d+1) ]

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(d+1):
    if i>0:
        dp[i] = min(dp[i],dp[i-1]+1)

    for j in range(len(arr)):
        start = arr[j][0]
        end = arr[j][1]
        dis = arr[j][2]
        if (i==start and end <= d):
            dp[end] = min(dp[end],dp[start]+dis)
print(dp[d])