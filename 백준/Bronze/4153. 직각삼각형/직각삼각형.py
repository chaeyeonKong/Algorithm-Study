import sys
input = sys.stdin.readline

while True:
    a,b,c= map(int,input().split())
    if (a==0 or b==0 or c==0) :
        break;
    max = a

    if a<b:
        max = b
    if max<c:
        max = c
    # print(max)
    if max == a:
        if b**2 + c**2 == max**2:
            print("right")
        else:
            print("wrong")
    elif max == b:
        if a**2 + c**2 == max**2:
            print("right")
        else:
            print("wrong")
    elif max == c:
        if b**2 + a**2 == max**2:
            print("right")
        else:
            print("wrong")


