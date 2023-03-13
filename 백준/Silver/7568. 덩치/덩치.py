import sys
input = sys.stdin.readline
a = int(input()[:-1])
li=[]; ret = []
for i in range(a):
    x,y = map(int,input().split())
    li.append((x,y))
for i in range(a):
    cnt=1
    for j in range(a):
        if li[i][0] < li[j][0]:
            if li[i][1] < li[j][1]: cnt+=1
    ret.append(str(cnt))
print(*ret)