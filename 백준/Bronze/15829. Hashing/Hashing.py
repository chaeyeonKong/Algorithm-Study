import sys
n = int(sys.stdin.readline().strip())
arr = list(sys.stdin.readline().strip())
ans=0

for i in range(len(arr)):
    ans += (ord(arr[i])-96) * (31**i)

print(ans%1234567891)