import sys
input = sys.stdin.readline

n,m = map(str,input().split())
n=n[::-1]
m=m[::-1]
ret = int(str(int(n)+int(m))[::-1])
print(ret)