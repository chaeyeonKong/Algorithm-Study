import sys
input = sys.stdin.readline
ret = False
rank=1
n,new,p = map(int,input().split())
li = sorted(list(map(int,input().split())),reverse=True)

if (n==p and new<= li[len(li)-1]):
    print(-1)
else:
    for i in range(len(li)):
        if new < li[i]:
            rank+=1
        else:
            break
    print(rank)