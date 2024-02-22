import sys
n = int(sys.stdin.readline().strip())
n_li = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
m_li = list(map(int,sys.stdin.readline().split()))

dic = dict()

for i in n_li:
    if i in dic:
        dic[i]+=1
    else:
        dic[i] = 1

for i in range(m):
    if m_li[i] in dic:
        print(dic[m_li[i]],end=' ')
    else:
        print(0, end = ' ')