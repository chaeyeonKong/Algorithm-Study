import sys
n = int(sys.stdin.readline().strip())

dis = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

ret = price[0] * dis[0]
a = price[0]

for i in range(1,n-1):
    if price[i] < a:
        a = price[i]

    ret+=(dis[i]*a)
print(ret)
