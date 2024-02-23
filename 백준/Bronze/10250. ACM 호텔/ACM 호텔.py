import sys
k = int(sys.stdin.readline().strip())

for i in range(k):
    h, w, n = map(int,sys.stdin.readline().split())
    arr = [[0] * w] * h

    if n%h==0:
        floor=h #층
        cnt = n//h  # 호실
    else:

        floor = n%h
        cnt = (n//h)+1

    print(((floor*100)+cnt))