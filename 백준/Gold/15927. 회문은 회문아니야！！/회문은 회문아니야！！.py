import sys
input = sys.stdin.readline

txt = input()[:-1]

if len(set(txt))==1:    print(-1)
elif txt == txt[::-1]:    print(len(txt) - 1)
else:    print(len(txt))