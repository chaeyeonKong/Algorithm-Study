import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    k = int(sys.stdin.readline().strip())

    a, b = 1, 0
    for i in range(k):
        a,b = b,(a+b)
    print(a,b)