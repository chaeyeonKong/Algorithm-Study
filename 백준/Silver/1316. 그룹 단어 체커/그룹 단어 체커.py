import sys
input = sys.stdin.readline
n = int(input())
cnt=n; ret=''

for i in range(n):
    txt = input()[:-1]; ret=''
    for j in range(len(txt)):
        if j>0:
            if ret[len(ret)-1] != txt[j] and txt[j] in ret:
                cnt-=1; break
            else: ret += txt[j]
        else:
            ret += txt[j]
print(cnt)