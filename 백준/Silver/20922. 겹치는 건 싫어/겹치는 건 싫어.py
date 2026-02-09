import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dict = {}
ret = []
idx = 0

left = 0
right = 0

for i in range(n):
    el = arr[right]
    if el not in dict:
        dict[el] = 1
    else:
        dict[el] += 1

    while(dict[el]>k): # 슬라이딩 윈도우가 깨졌을 때 이걸로 left를 이동하는게 핵심
        if arr[left] in dict:
            dict[arr[left]]-=1
        left +=1
    ret.append(right - left + 1)
    right+=1

# print(ret)
print(max(ret))
