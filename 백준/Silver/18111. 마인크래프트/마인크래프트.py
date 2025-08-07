## 마인크래프트
import sys

n,m,b = map(int,sys.stdin.readline().split())
arr = []
ans = (1e9)
glevel = 0

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(257):
    take_block = 0
    use_block = 0

    for x in range(n):
        for y in range(m):
            if arr[x][y] > i:
                take_block += arr[x][y]-i
            else:
                use_block += i - arr[x][y]

    if use_block > take_block + b:
        continue

    count = take_block*2 + use_block

    if count <= ans:
        ans = count
        glevel = i


print(ans, glevel)

