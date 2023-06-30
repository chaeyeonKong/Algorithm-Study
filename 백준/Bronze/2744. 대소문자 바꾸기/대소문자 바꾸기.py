import sys
txt = sys.stdin.readline()[:-1]
ret=''
for i in txt:
    if i.isupper(): i = i.lower()
    else: i = i.upper()
    ret = ret+i
print(ret)