import sys
N = int(sys.stdin.readline()[:-1])
stone=N
i=1
while(True):
    if stone>4: stone-=3
    else: stone-=1
    i += 1
    if stone==0:
        if i%2==0: print("SK")
        else: print("CY")
        break