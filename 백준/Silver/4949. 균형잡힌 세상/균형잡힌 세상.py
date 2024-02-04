import sys
arr = list(sys.stdin.readline())
while(arr[0]!='.'):

    s = [] #stack

    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] == '[':
            s.append(arr[i])
        elif arr[i] ==')':
            if len(s)!=0 and s[-1]=='(':
                s.pop()
            else:
                s.append(arr[i])
                break
        elif arr[i]==']':
            if len(s)!=0 and s[-1]=='[':
                s.pop()
            else:
                s.append(arr[i])
                break

    if len(s)==0:
        print('yes')
    else:
        print('no')
    arr = list(sys.stdin.readline())