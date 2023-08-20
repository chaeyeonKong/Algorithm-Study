import sys
n = int(sys.stdin.readline()[:-1])
arr=[]
for i in range(n):
    a, b = map(int, sys.stdin.readline()[:-1].split())
    arr.append([a,b])
arr.sort()
cost = 10001
result=0
for i in arr:
    temp = i[1]
    if temp < cost:
        cost = temp
        result +=1
print(result)