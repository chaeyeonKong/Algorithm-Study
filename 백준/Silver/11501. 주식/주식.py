import sys
n = int(sys.stdin.readline().strip())
for _ in range(n):
    k = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    buy = []
    ret = []
    target= arr[k-1]
    idx = k-2
    while(True):
        if arr[idx] < target:
            buy.append(arr[idx])
        else:
            ret.append((target*len(buy)) - sum(buy))
            buy=[]
            target = arr[idx]
        idx-=1
        if idx<0:
            ret.append((target*len(buy)) - sum(buy))
            break
    print(sum(ret))
