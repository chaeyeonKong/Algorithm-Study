import sys
input = sys.stdin.readline
N = int(input())
arr=[]
for i in range(N):
    txt = input()[:-1]
    arr.append(txt)
arr = list(set(arr))
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)