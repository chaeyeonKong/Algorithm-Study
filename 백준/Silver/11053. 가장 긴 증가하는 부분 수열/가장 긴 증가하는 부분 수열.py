import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))


dp = [1]*n

for i in range(1,n):
    temp = []
    for j in range(0,i):
        if arr[j] < arr[i]:
            temp.append(dp[j])
    if temp!=[]:
        dp[i] = max(temp)+1


print(max(dp))