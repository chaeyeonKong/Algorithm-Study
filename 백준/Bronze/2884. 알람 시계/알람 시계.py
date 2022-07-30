a,b  = map(int, input().split())

b = b-45
if b<0 :
    b=b+60
    if a==0:
        a = 23
    else:
        a=a-1

print("%d %d"%(a,b))