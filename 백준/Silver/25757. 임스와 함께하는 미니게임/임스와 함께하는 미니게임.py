import sys
n, game = map(str, sys.stdin.readline().split())
n = int(n)
arr = {}

for i in range(n):
    name = sys.stdin.readline().strip()
    arr[name]=1

ans = len(arr)
if game=='Y':
    print(ans//1)
elif game == 'F':
    print(ans // 2)
else:
    print(ans // 3)