import sys
n, m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

sum = a[0]
left = 0
right = 1

cnt = 0

while(True):
    if sum<m:
        if right < n:
            sum+=a[right]
            right+=1
        else:
            break
    elif sum==m:
        cnt+=1
        sum-=a[left]
        left+=1
    else:
        sum-=a[left]
        left+=1

print(cnt)