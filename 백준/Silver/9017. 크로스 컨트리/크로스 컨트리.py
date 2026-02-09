import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    k = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    kk = len(set(arr))
    ans = {}

    dict= {} # 개수 세기
    li = [] # 포함 리스트
    for el in arr: # 개수 세기
        if el not in dict:
            dict[el]= 1
        else:
            dict[el]+=1

    for el in dict: #6개인거만 li에 넣기
        if dict[el] ==6:
            li.append(el)

    ret = {}
    idx = 1

    for j in range(k):
        if arr[j] in li:
            if arr[j] not in ans:
                ans[arr[j]] = []
            ans[arr[j]].append(idx)
            idx+=1

    minn = 10**9
    minidx = -1
    la = []
    # print(ans)
    for team in ans:
        s = sum(ans[team][:4]) # 상위 4명의 점수만 합해야지.....
        if s < minn:
            minn = s
            minidx = team
            la = [team]
        elif s == minn:
            la.append(team)

    if len(la)==1:
        print(minidx)
    else:
        real = []
        for j in la:
            real.append((j, ans[j][4]))
        # print(real)
        real.sort(key = lambda x:x[1])
        print(real[0][0])