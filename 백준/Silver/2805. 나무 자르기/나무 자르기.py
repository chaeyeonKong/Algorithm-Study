import sys

n,m = map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))
start, end = 0,max(tree)

while start<=end:
    ret=0
    mid = ((start+end)//2)

    for el in tree:
        if el>mid:
            ret += el-mid

    if ret >= m:
        start=mid+1
    else:
        end=mid-1

print(end)