import sys
n,k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

dict = {}
left = 0
right = 0
ret = []
for i in range(n):
    if arr[right] not in dict:
        dict[arr[right]]  = 1
    else:
        dict[arr[right]] += 1


    while(dict[arr[right]]>k):
        dict[arr[left]]-=1
        left+=1
    ret.append(right-left+1)
    right+=1
print(max(ret))