import sys
input = sys.stdin.readline
a,b,last = map(int,input().split())
k = (last-b)/(a-b)
print(int(k) if k==int(k) else int(k)+1)