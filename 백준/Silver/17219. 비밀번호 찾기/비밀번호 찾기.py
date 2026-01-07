import sys
a,b = map(int, sys.stdin.readline().split())
dict = {}
for _ in range(a):
    s, pw = map(str, sys.stdin.readline().split())
    dict[s] = pw

for i in range(b):
    target = sys.stdin.readline().strip()
    print(dict[target])
