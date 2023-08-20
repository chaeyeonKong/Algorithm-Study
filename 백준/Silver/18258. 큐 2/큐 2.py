import sys
from collections import deque

a= int(sys.stdin.readline()[:-1])
queue = deque()
#앞에 넣은걸 빼는 구조 , FIFO
for i in range(a):
    txt = sys.stdin.readline()[:-1]
    if txt[:2]=="pu":
        queue.append(int(txt.split()[1]))
    elif txt=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif txt == 'size':
        print(len(queue))
    elif txt == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif txt == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[len(queue)-1])