import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

stack = []
li = [0] * n

for i in range(n):

    while stack and stack[-1][1]<arr[i]:
        stack.pop()

    if stack:
        li[i] = stack[-1][0]+1

    stack.append((i,arr[i]))

print(*li)