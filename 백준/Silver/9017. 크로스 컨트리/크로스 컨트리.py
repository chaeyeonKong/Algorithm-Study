import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    k = int(input().strip())
    arr = list(map(int, input().split()))

    cnt = {}
    for el in arr:
        cnt[el] = cnt.get(el, 0) + 1

    li = []
    for el in cnt:
        if cnt[el] == 6:
            li.append(el)

    ans = {} 
    idx = 1
    for j in range(k):
        if arr[j] in li:
            if arr[j] not in ans:
                ans[arr[j]] = []
            ans[arr[j]].append(idx)
            idx += 1

    minn = 10**9
    cand = []

    for team in ans: 
        s = sum(ans[team][:4])
        if s < minn:
            minn = s
            cand = [team]
        elif s == minn:
            cand.append(team)

    if len(cand) == 1:
        print(cand[0])
    else:
        cand.sort(key=lambda x: ans[x][4])
        print(cand[0])
