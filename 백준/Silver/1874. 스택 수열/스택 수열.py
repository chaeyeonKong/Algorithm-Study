import sys

n = int(sys.stdin.readline().strip())
s = []  # stack
answer = ''
max_int = 1

for i in range(n):
    num = int(sys.stdin.readline().strip())

    for j in range(max_int,num+1):
        s.append(j)
        answer += "+\n"
        max_int += 1

    if s[-1]==num:
        s.pop()
        answer += "-\n"

if len(s) != 0:
    print("NO")
else:
    print(answer)