import sys

num = int(sys.stdin.readline().strip())

for i in range(num):
    n, r = map(int, sys.stdin.readline().strip().split())
    ret=1
    k=1
    
    for j in range(r, r-n,-1):
        ret = ret*j
        ret = ret/k
        k+=1
        
    print(int(ret))




