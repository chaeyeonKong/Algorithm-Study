import sys

txt = sys.stdin.readline().strip()
txt = txt.replace('XXXX','AAAA')
txt = txt.replace('XX','BB')

if 'X' in txt:
    print(-1)
else:
    print(txt)