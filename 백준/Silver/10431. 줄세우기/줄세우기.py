import sys
n = int(sys.stdin.readline().strip())

arr = []
ans = []

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for el in arr:
    cnt = 0
    ans = []

    for i in range(len(el)):
        if i>0:
            if ans==[]:
                ans.append(el[i])
            else:
                idx = len(ans)-1
                while(ans[idx]>el[i]):
                    if el[i] < ans[idx]:
                        cnt+=1
                    idx -= 1
                    if idx<0:break

                ans.append(el[i])
        ans.sort()
    print(el[0], cnt)


