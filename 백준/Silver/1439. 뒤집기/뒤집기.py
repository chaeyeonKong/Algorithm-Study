import sys
input = sys.stdin.readline
N = input()[:-1]
cnt=0; tmp = int(N[0])

for i in range(len(N)):
    k = int(N[i])
    if i>0:
        tmp = int(N[i-1])
    if k!=tmp:
        cnt+=1

print((cnt+1)//2)