import sys
import math
l = int(sys.stdin.readline()[:-1])
a = int(sys.stdin.readline()[:-1])
b = int(sys.stdin.readline()[:-1])
c = int(sys.stdin.readline()[:-1])
d = int(sys.stdin.readline()[:-1])

hap1 = math.ceil(a/c)
hap2 = math.ceil(b/d)
print(l-max(hap1,hap2))