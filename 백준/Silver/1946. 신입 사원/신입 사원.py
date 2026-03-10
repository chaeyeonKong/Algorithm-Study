import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    k = int(sys.stdin.readline().strip())
    arr=[]
    cnt = 1
    for i in range(k):
        a,b = map(int, sys.stdin.readline().split())
        arr.append((a,b))

    arr.sort(key=lambda x:x[0])
    t_rank = arr[0][1]
    for i in range(1,k):
        if arr[i][1]<t_rank:
            t_rank = arr[i][1]
            cnt+=1

    print(cnt)
