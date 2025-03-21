import sys
n = int(sys.stdin.readline().strip())
arr = set()

for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if b=="enter":
        arr.add(a)
    else:
        arr.remove(a)

arr = sorted(arr, key = lambda x:x , reverse=True)


for em in arr:
    print(em)