import sys
from collections import deque

n = int(sys.stdin.readline().strip())
ret = []

for i in range(n):
    txt = sys.stdin.readline().strip()
    if ret != []:
        j = 0
        while (1):
            words = deque(ret[j])
            samecheck = 0
            for k in range(len(ret[j])):
                if words == deque(txt):
                    samecheck = 1
                    break
                else:
                    words.append(words[0])
                    words.popleft()
            j += 1
            if j > len(ret) - 1 or samecheck == 1: break

        if samecheck == 0:
            ret.append(txt)
    else:
        ret.append(txt)
        
print(len(ret))
