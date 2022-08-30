import sys
input = sys.stdin.readline
k = int(input())
slist = list(map(int,input().split()))
count=0

for i in range(len(slist)):
    if slist[i]<=1:
        count+=1
        continue
    for j in range(2,slist[i],1):
        if slist[i]%(j)==0:
            count+=1
            break

print(k-count)