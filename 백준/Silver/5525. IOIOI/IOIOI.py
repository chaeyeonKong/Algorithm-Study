import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
txt = list(sys.stdin.readline().strip())

cnt = 0
i = 0
pattern = 0

while i<k-1:
    if txt[i]=='I' and i+2 < k and txt[i+1]=='O' and txt[i+2]=='I':
        pattern+=1 # IOI 찾을 때 마다 증가
        if pattern == n:
            cnt+=1
            pattern -= 1
        i+=2 #마지막 I 포함해서 다시 탐색
    else:
        pattern = 0
        i+=1
        
print(cnt)
