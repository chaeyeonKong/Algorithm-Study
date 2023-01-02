import sys
input = sys.stdin.readline

n = int(input())
ret=set()

for  i in range(n):
    txt = input()[:-1]
    if txt=='all': ret = set([i+1 for i in range(20)])
    elif txt=='empty': ret = set()
    else:
        order, num = txt.split()
        num = int(num)
        if num in ret:
            if order == 'remove' or order == 'toggle': ret.remove(num)
            elif order == 'check': print(1)
        else:
            if order == 'add' or order == 'toggle': ret.add(num)
            if order == 'check': print(0)