import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    words={}
    m = int(sys.stdin.readline().strip())
    for j in range(m):
        a, b = sys.stdin.readline().split()
        if b in words:
            words[b].append(a)
        else:
            words[b] = [a]
    cnt = 1
    for el in words:
        cnt *= (len(words[el])+1)

    print(cnt-1)