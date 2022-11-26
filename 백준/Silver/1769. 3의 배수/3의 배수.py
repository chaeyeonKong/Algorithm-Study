import sys
input = sys.stdin.readline
N = str(input()[:-1])
hap=0;cnt=0
ret=""; short=False
if len(N)==1:
    short=True
while(True):
    for i in range(len(N)):
        hap+=int(N[i])
    cnt+=1
    if hap<10:
        if hap%3==0:
            ret="YES"
        else:
            ret="NO"
        break
    else:
        N = str(hap)
        hap = 0
if short==True:
    cnt=0
print(cnt)
print(ret)