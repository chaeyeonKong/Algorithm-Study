import sys

n = int(sys.stdin.readline().strip())
txt = []
ret = []
for tc in range(2):
    arr = [[] for i in range(n+2)]
    visited = [[0]*(n+2) for i in range(n+2)]
    arr[0] = ["-1" for _ in range(n+2)] # 맨 윗줄 패딩
    arr[n+1] = ["-1" for _ in range(n+2)] # 맨 아랫줄 패딩

    for i in range(n):
        if tc == 0:
            tx = sys.stdin.readline().strip()
            txt.append(tx)
            target = list(tx)
        else:
            target = list(str(txt[i]).replace("G", "R"))
        arr[i + 1] = ["-1"] + target + ["-1"]  # 좌우 패딩 추가

    # ----------- 세팅 완료

    stack = []
    move = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if visited[i][j] == 0:  # 방문하지 않은 노드만 처리
                stack.append([i, j])
                check = 0
                while stack:
                    si, sj = stack.pop()
                    base = arr[si][sj]
                    if visited[si][sj] == 0:
                        visited[si][sj] = 1
                        for k in range(4):
                            x = si + move[k][0]
                            y = sj + move[k][1]
                            target = arr[x][y]
                            if base == target:
                                stack.append([x, y])
                ans += 1
    ret.append(ans)

print(*ret)