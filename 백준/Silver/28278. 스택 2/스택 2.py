import sys
N = int(sys.stdin.readline()[:-1])
stack = []
for i in range(N):
    order = sys.stdin.readline()[:-1]
    x = int(order[:1])

    if x==1:
        a,b = order.split()
        stack.append(b)
    elif x==2:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)

    elif x == 3:
        print(len(stack))
    elif x == 4:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])