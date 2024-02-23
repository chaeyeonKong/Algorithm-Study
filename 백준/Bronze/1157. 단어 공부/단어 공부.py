import sys
txt = list(sys.stdin.readline().split())

dic = dict()

for i in range(len(txt[0])):
    target = txt[0][i].upper()
    if dic.get(target):
        dic[target]+=1
    else:
        dic[target] = 1

dic = sorted(dic.items(), key=lambda item:item[1],reverse=True)
if len(dic)>1:
    if dic[0][1] == dic[1][1]:
        print('?')
    else:
        print(dic[0][0])
else:
    print(dic[0][0])
