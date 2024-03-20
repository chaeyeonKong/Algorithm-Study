import sys
n = int(sys.stdin.readline().strip())
arr=[]; ret = []
for i in range(n):
    k = int(sys.stdin.readline().strip())
    arr.append(k)

arr = sorted(arr)

for i in range(len(arr)):
    ret.append(arr[i]*n)
    n-=1
ret = sorted(ret)
print(ret[-1])