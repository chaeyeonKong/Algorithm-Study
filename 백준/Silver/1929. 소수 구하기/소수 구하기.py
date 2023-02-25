import sys
input = sys.stdin.readline

a, b = map(int,input().split())
arr = [i for i in range(2,b+1)]

for i in range(len(arr)):

    if arr[i]==0: continue
    for j in range(i+arr[i],len(arr),arr[i]):
        arr[j]=0

for i in range(len(arr)):
    if arr[i]!=0 and arr[i] >=a and arr[i] <=b:
        print(arr[i])