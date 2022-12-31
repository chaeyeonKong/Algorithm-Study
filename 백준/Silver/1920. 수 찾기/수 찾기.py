import sys
input = sys.stdin.readline

n = int(input())
arr1 = set(map(int,input()[:-1].split()))
n = int(input())
arr2 = list(map(int,input()[:-1].split()))

for i in range(len(arr2)):
    if arr2[i] in arr1: print(1)
    else: print(0)