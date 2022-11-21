import sys
input = sys.stdin.readline
N = int(input())
a=[]
b=[]
s=0

a = sorted(list(map(int,input().split())))
b = sorted(list(map(int, input().split())),reverse=True)

for i in range(N):
    s += a[i] * b[i]

print(s)