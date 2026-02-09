import sys
n,d,k,c = map(int, sys.stdin.readline().split())

li = []
for i in range(n):
    li.append(int(sys.stdin.readline().strip()))

check = [0] * (d+1)
check[c] = 1
eat = 1
max_s = 0
for i in range(k):
    s = li[i%n]
    if check[s]==0:
        eat+=1
    check[s] += 1

max_s = eat

for i in range(n):
    left = li[i%n]
    right = li[(i+k)%n]

    check[left]-=1
    if check[left]==0:
        eat -=1
    check[right] += 1
    if check[right]==1:
        eat+=1
    max_s = max(max_s, eat)
print(max_s)