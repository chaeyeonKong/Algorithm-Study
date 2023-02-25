import sys
input = sys.stdin.readline
a = int(input()[:-1])

for i in range(a):
    k = int(input()[:-1]) #층
    n = int(input()[:-1]) #호수
    p=[i for i in range(1,n+1)]

    for j in range(k):
        for l in range(1,n):
            p[l] += p[l-1]
    print(p[-1])