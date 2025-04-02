import sys
n, l = map(int, sys.stdin.readline().split())
l-=1 # (좌우 0.5씩 추가해줘야 하기 때문에)

arr = list( map(int, sys.stdin.readline().split()))
arr = sorted(arr)

tape = 1
end = arr[0] + l

for i in range(1,n):
    if end < arr[i]:
        tape+=1
        end = arr[i] + l

print(tape)
