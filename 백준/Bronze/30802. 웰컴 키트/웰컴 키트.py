import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
t,p = map(int,sys.stdin.readline().split())

count=0

for el in arr:
    localT = t
    if el>0:
        if el%localT>0:
            count += (el//localT)+1
        else:
            count += el // localT

print(count)
print(n//p, n%p)