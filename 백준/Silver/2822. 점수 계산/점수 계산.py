import sys
arr = []
arr2=[]
ret=[]
for i in range(8):
    arr.append(int(sys.stdin.readline().strip()))

arr2 = arr.copy()
arr.sort()
arr = arr[::-1]

sum=0
for i in arr:
    sum+=i
    ret.append(arr2.index(i)+1)
    if len(ret)==5:break

ret.sort()
print(sum)
print(*ret)