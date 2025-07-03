import sys

p = 'I'
plus = 'OI'

n = int(sys.stdin.readline().strip())
p+=n*plus

k = int(sys.stdin.readline().strip())
txt = list(sys.stdin.readline().strip())

cnt = 0
for i in range(k):
    if txt[i]=='I':
        if txt[i:i+len(p)]==list(p):
            cnt+=1

print(cnt)