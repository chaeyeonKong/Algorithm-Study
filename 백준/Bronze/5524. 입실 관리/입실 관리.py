import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    str = input().lower()
    print(str[:-1])