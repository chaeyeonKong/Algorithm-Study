import sys
a,b = map(int,sys.stdin.readline()[:-1].split())
A = sys.stdin.readline()[:-1].split()
B = sys.stdin.readline()[:-1].split()

ret1 = set(A)-set(B)
ret2 = set(B) - set(A)
print(len(ret1)+len(ret2))