import sys

k = int(sys.stdin.readline().strip())
memo = [(1,0),(0,1)]
for i in range(2,k+1):
    memo.append((memo[i-2][0] + memo[i-1][0], memo[i-2][1] + memo[i-1][1]))
    
print(memo[k][0],memo[k][1])