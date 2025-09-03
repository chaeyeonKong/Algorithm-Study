import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(str,sys.stdin.readline().strip()))
length = len(arr)

visited = [False for _ in range(length)]
cnt = 0

for i in range(0,n):
    if arr[i]=='P':
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and arr[j] == 'H' and not visited[j]:
                visited[j] = True
                cnt += 1
                break
print(cnt)