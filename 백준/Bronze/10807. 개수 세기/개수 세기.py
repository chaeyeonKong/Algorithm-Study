import sys
import math
input = sys.stdin.readline
N = int(input())
l = list(map(int,input().split()))
dic = dict.fromkeys(l,0)
find = int(input())
for i in range(N):

    dic[l[i]]+=1

re = dic.get(find)
if re == None:
    print(0)
else:
    print(re)