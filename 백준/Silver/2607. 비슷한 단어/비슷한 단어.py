import sys
n = int(sys.stdin.readline().strip())
boss = list(sys.stdin.readline().strip())
ans = 0
for i in range(1,n):
    compare = boss[:]
    el = sys.stdin.readline().strip()
    cnt = 0

    for em in el:
        if em in compare:
            compare.remove(em)
        else:
            cnt+=1
    if cnt<2 and len(compare)<2:
        ans+=1
print(ans)