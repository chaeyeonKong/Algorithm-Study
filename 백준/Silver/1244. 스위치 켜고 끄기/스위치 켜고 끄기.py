import sys

n = int(sys.stdin.readline().strip())

button = list(map(int, sys.stdin.readline().split()))

k = int(sys.stdin.readline().strip())

for _ in range(k):
    sex, idx = map(int, sys.stdin.readline().split())

    if sex==1: #남성
        for i in range(idx,n+1,idx):
            if button[i-1]==0:
                button[i - 1]=1
            else:
                button[i - 1]=0

    else:
        idx-=1
        start = idx
        end = idx

        while(0<=start-1 and end+1<n and button[start-1] == button[end+1]):
            start-=1
            end+=1

        for i in range(start, end+1):
            if button[i]==0:
                button[i] = 1
            else:
                button[i] = 0

for i in range(n):
    if i!=0 and i%20==0:
        print()
    print(button[i], end = " ")
