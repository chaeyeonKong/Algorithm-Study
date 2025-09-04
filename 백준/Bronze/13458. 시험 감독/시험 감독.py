import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
a,b = map(int, sys.stdin.readline().split())

ans = 0

for i in range(n):
    if arr[i]-a<=0:
        ans+=1
    else:
        ans+=1
        k = arr[i]-a
        if k%b==0:
            ans += k // b
        else:
            ans += (k // b)+1
print(ans)