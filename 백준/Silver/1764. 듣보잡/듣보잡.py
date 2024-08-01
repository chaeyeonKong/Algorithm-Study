import sys

n,m = map(int,sys.stdin.readline().split())
arr1 = dict()
ans = []
# 듣도 보도 못한 사람 n
# 보도 못한 사람 m


for i in range(n):
    x = sys.stdin.readline().strip()
    if x not in arr1:
        arr1[x] = i

for i in range(m):
    target = sys.stdin.readline().strip()
    if target in arr1:
        ans.append(target)

ans = sorted(ans)

print(len(ans))
for el in ans:
    print(el)