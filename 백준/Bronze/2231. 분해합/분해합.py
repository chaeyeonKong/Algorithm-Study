
import sys
input = sys.stdin.readline
n = int(input())
ret=0

for i in range(1,n):
    if n == sum(map(int,str(i))) + i :
        ret = i
        break
print(ret)