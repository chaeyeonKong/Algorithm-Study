import sys
n = int(sys.stdin.readline().strip())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))
arr = sorted(arr)
# ----------------------------------------------------------------
#산술 평균
print(round(sum(arr)/len(arr)))
#중앙값
print(arr[len(arr)//2])
# ----------------------------------------------------------------
dic = dict().fromkeys(set(arr))
count=0 # 최빈값 중복인가?
for i in range(n):
    if not dic[arr[i]]:
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1

#최빈순 정렬
dic =sorted(dic.items(), key = lambda item:item[1], reverse=True)
be=dic[0][1] # 비교대상

li=[]
li.append(dic[0][0])
for i in range(1,len(dic)):
    if dic[i][1]== be:
        li.append(dic[i][0])
li = sorted(li)

if len(li)>1:
    print(li[1])
else:
    print(li[0])

#범위
print(arr[len(arr)-1] - arr[0])