import sys

while(True):
    gubun = 'Junior'
    input = sys.stdin.readline
    a,b,c = input().split()
    if a=='#' and int(b) ==0 and int(c)==0:
        break
    else:
        if int(b)>17 or int(c)>=80:
            gubun = 'Senior'
        print("%s %s"%(a,gubun))