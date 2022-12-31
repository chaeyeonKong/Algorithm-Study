import sys
input = sys.stdin.readline
N = int(input())
n = N
new = -1; i=0

while(True):
    i+=1
    n1 = n//10
    n2 = n%10
    hap = n1+n2
    if hap>=10:
        hap = str(hap)[1]
    new = str(n2) + str(hap)
    if int(new) == N:
        print(i)
        break
    n = int(new)