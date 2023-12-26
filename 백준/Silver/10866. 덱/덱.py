import sys
from collections import deque

n = int(sys.stdin.readline().strip())
dq = deque()

for i in range(n):
        data = list(map(str, sys.stdin.readline().split()))
        if data[0] == 'push_front':
                dq.appendleft(int(data[1]))
        elif data[0] == 'push_back':
                dq.append(int(data[1]))
        elif data[0] == 'pop_front':
                if len(dq)>0:
                        print(dq.popleft())
                else:
                        print(-1)
        elif data[0] == 'pop_back':
                if len(dq)>0:
                        print(dq.pop())
                else:
                        print(-1)
        elif data[0] == 'size':
                print(len(dq))
        elif data[0] == 'empty':
                if len(dq)==0:
                     print(1)
                else:
                     print(0)

        elif data[0] == 'front':
                if len(dq)>0:
                        print(dq[0])
                else:
                        print(-1)
        elif data[0] == 'back':
                if len(dq) > 0:
                        print(dq[len(dq)-1])
                else:
                        print(-1)