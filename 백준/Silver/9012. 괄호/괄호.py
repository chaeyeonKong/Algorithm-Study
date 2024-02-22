import sys, queue
n= int(sys.stdin.readline().strip())
s = [] #stack

for _ in range(n):
    arr = list(map(str,sys.stdin.readline().strip()))
    ans = 'YES'
    s=[]
    for i in range(len(arr)):
        if arr[i] == ')':
            if len(s)>0:
                s.pop()
            else:
                ans = 'NO'
                break
        else:
            s.append(arr[i])

    if s:
        ans = 'NO'

    print(ans)