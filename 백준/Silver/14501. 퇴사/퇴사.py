import sys

n = int(sys.stdin.readline().strip())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+arr[i][0] , n+1): # 그냥 마지막으로 업데이트 시켜버리려고 모두 넣는군..
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]
print(dp[-1])