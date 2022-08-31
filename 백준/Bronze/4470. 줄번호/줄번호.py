import sys
input = sys.stdin.readline
k = int(input())
for i in range(k):
    text = input()[:-1]
    print("%d. %s"%(i+1,text))