import sys
n = int(sys.stdin.readline().strip())
txt = 666
cnt=0

while(True):
    if '666' in str(txt):
        cnt+=1
    if cnt == n:
        break
    txt += 1
    
print(txt)