import sys, queue
n, k = map(int,sys.stdin.readline().split())
arr = [i+1 for i in range(n)]

ans=[]
num = 0

for i in range(n):
    num += k-1
    if num>=len(arr):
        num = num %len(arr)

    ans.append(arr.pop(num))

print("<",end='')
for i in range(n):

    if i==n-1:
        print(ans[i], end='')
    else:
        print(ans[i], end=', ')
print(">")