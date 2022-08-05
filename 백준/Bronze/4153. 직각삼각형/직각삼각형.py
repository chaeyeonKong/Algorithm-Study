import sys
input = sys.stdin.readline

while True:
    Nlist= list(map(int,input().split()))

    if (Nlist[0]==0 or Nlist[1]==0 or Nlist[2]==0) :
        break;
    NList = sorted(Nlist,reverse=True)

    if(NList[0]**2 == NList[1]**2 + NList[2]**2):
        print("right")
    else:
        print("wrong")