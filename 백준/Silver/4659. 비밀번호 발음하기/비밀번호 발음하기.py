import sys
arr = ['a','e','i','o','u']
while(True):
    check = False
    txt = str(sys.stdin.readline().strip())
    if txt=='end':
        break
    cnt = 0
    gubun = -1
    ans = True
    for el in txt:
        if el in arr:
            check = True
        if el in arr:
            if gubun==1:
                cnt = 0
            cnt +=1
            gubun = 0
        else:
            if gubun==0:
                cnt = 0
            cnt +=1
            gubun = 1
        if cnt == 3:
            ans = False
            break
    for i in range(1,len(txt)):
        if txt[i] == txt[i-1] and (txt[i]!='o' and txt[i]!='e'):
            ans = False
            break

    if ans and check:
        print("<%s> is acceptable."%(txt))
    else:
        print("<%s> is not acceptable."%(txt))

