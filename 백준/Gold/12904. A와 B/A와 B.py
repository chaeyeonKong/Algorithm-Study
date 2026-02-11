import sys
s = str(sys.stdin.readline().strip())
t = str(sys.stdin.readline().strip())
ret = 0

while(len(s) <= len(t)):
    alpha = t[-1]
    t = t[:len(t) - 1]
    if alpha=='B':
        t=t[::-1]

    if t==s:
        ret = 1
        break
print(ret)