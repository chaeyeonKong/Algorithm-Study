import sys , collections
input = sys.stdin.readline

N = int(input())
arr=[]

for i in range(N):
    order=input()[:-1]
    if order[:4] == 'push':
        num = int(order[5:])
        arr = arr[::-1]
        arr.append(num)
        arr = arr[::-1]
    elif order=='pop':
        if len(arr)!=0:
            print(arr[len(arr)-1])
            arr.pop()
        else:
            print(-1)
    elif order=='size':
        print(len(arr))
    elif order=='empty':
        if len(arr)==0:
            print(1)
        else:
            print(0)
    elif order=='front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])
    elif order=='back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
