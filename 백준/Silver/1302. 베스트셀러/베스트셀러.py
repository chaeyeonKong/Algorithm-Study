import sys
input = sys.stdin.readline
N = int(input())
dic = {}
arr = []

for i in range(N):
    target = input()[:-1]
    try:
         dic[target]+=1
    except:
        dic[target]=1

k = max(dic.values())
#print(dic)
for i in dic:
    if dic[i]==k:
        arr.append(i)

print(sorted(arr)[0])