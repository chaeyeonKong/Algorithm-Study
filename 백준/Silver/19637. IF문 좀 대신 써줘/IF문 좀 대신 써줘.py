import sys
n,m = map(int,sys.stdin.readline().split())

arr = []
for _ in range(n):
    li = list(sys.stdin.readline().split())
    arr.append([li[0],int(li[1])])

for i in range(m):
    k = int(sys.stdin.readline().strip())

    # 이분 탐색
    start = 0
    end = n
    mid = (start + end) // 2
    while(start<=end):
        if k <= arr[mid][1]:
            end = mid-1
        elif k > arr[mid][1]:
            start = mid+1
        mid = (start + end) // 2
    print(arr[start][0])
