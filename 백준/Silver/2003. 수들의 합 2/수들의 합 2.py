import sys
n, m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

sum = arr[0]
left = 0
right = 1
cnt = 0

while(True):
    if sum < m:
        if right < n:
            sum+= arr[right]
            right +=1
        else:
            break
    elif sum==m:
        cnt+=1
        sum -= arr[left]
        left+=1
    else:
        sum-=arr[left]
        left+=1
print(cnt)
