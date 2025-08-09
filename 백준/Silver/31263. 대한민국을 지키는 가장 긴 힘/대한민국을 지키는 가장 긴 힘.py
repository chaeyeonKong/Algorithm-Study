import sys
from collections import deque

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

q = deque(s)

idx = 0
cnt = 0
while(q):

    lenn = min(3,len(q))
    ret = ''
    for _ in range(lenn):
        ret+=q.popleft()

    idx = 2
    if int(ret)>641:
        q.appendleft(ret[idx])
        idx-=1
    else:
        cnt += 1
        if q:
            while(True):
                if q[0]=='0':
                    q.appendleft(ret[idx])
                    idx-=1
                else:
                    break



print(cnt)