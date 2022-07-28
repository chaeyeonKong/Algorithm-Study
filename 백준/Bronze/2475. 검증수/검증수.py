import math
a,b,c,d,e =  map(int,input().split())
print(int((math.pow(a,2) + math.pow(b,2) + math.pow(c,2) + math.pow(d,2) +math.pow(e,2))%10))
