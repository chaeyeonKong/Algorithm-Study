import sys
input = sys.stdin.readline
N= int(input())
num = [0]*N

for i in range(N):
    num[i]=int(input())

num = sorted(num)
for i in range(N):
    print(num[i])
