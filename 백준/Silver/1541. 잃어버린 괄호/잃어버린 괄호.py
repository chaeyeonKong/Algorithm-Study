import sys

arr = sys.stdin.readline().strip().split('-')
ret=[]
for el in arr:
    k = 0
    temp = el.split("+")
    for te in temp:
        k += int(te)
    ret.append(k)

n = ret[0]

for i in range(1,len(ret)):
    n-=ret[i]
print(n)