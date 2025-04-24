import sys
n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    s = sys.stdin.readline().strip()

    summ = 0
    for i in s:
        if i.isdigit():
            summ+=int(i)
    arr.append((s,summ))

arr = sorted(arr, key= lambda x:(len(x[0]), x[1], x[0]))
for i in range(n):
    print(arr[i][0])
