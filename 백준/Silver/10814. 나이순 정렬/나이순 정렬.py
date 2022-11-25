import sys
input = sys.stdin.readline
N = int(input()[:-1])
dic = []
for i in range(N):
    txt = input()
    age, name = txt.split()
    dic.append([age, name])

dic.sort(key = lambda x : int(x[0]))

for i in range(N):
    print("{} {}".format(dic[i][0],dic[i][1]))