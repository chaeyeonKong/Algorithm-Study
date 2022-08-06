import sys
input = sys.stdin.readline
result=""
N1 = int(input())
data = list(map(int,input().split()))
dic_data = dict.fromkeys(data,0)
for i in range(len(data)):
    dic_data[data[i]] +=1

N2 = int(input())
find = list(map(int,input().split()))

for i in range(N2):
    re = str(dic_data.get(find[i]))
    if re == "None": re = str(0)

    result += re + " "
print(result)

