import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr1=[];arr2=[]
for i in range(n):
    arr1.append(list(map(int,input().split())))

m,k = map(int,input().split())
for i in range(m):
    arr2.append(list(map(int,input().split())))

for i in range(n):
    ret=[]
    for j in range(k):
        hap=0
        for l in range(m):
            hap += arr1[i][l] * arr2[l][j]
        ret.append(hap)
    print(*ret)