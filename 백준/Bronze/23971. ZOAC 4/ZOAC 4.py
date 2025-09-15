import sys
import math
h,w,n,m = map(int, sys.stdin.readline().split())
n+=1
m+=1
print(math.ceil(h/n) * math.ceil(w/m))

