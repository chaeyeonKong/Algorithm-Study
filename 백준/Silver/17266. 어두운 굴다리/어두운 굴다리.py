import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0

if m ==1:
    ans = max(arr[0], n-arr[0])
else:
    for i in range(m):
        if i == 0:
            x = arr[i]
        elif i==m-1:
            x = n - arr[i]
        else:
            distance = arr[i]-arr[i-1]

            if distance%2==0:
                x = distance//2
            else:
                x = distance//2 +1

        ans = max(ans, x)

print(ans)