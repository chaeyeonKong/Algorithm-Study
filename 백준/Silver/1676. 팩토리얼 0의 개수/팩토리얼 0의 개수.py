import sys
n = int(sys.stdin.readline().strip())
def fact(n):
    ret = 1
    for i in range(n,1,-1):
        ret *= i
    return ret
cnt=0
for x in str(fact(n))[::-1]:
    if x != '0':
        break
    cnt += 1
print(cnt)