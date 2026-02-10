import sys

n,d,k,c = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))


check = [0]*(d+1)
check[c] = 1
eat = 1

for i in range(k):
    s = arr[i%n]
    check[s]+=1
    if check[s]==1:
        eat +=1
max_s = eat

for i in range(n):
    left = arr[i%n]
    right = arr[(i+k)%n]

    if check[left]==1:
        eat-=1
    check[left]-=1
    if check[right]==0:
        eat+=1
    check[right]+=1

    max_s = max(max_s, eat)

print(max_s)
