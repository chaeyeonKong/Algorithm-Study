M = 0
for i in range(9):
    num=int(input())
    if num > M:
        M = num
        idx = i

print(M)
print(idx+1)