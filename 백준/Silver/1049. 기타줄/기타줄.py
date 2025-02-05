import sys

# 6개 set, 1개씩
# 사야할 개수, 브랜드 개수
# 패키지 가격, 낱개 가격
# 패키지랑 낱개를 합쳐서 살 수 있지..

n,m = map(int, sys.stdin.readline().split())
arr1 = []
arr2 = []

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    arr1.append(a)
    arr2.append(b)

arr1.sort() # 6개 패키지
arr2.sort() #낱개

ret = 0
if arr1[0] == 0 or arr2[0]==0:
    ret = 0
else:

    ret = arr1[0] * int(n/6)
    k = min(arr2[0] * int(n%6) , arr1[0])
    ret += k
    if ret > arr2[0] * n:
        ret = arr2[0]*n
print(ret)