import sys

n = int(sys.stdin.readline().strip())
det = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

arr = []
ans_arr=[]
su = 9
ret=0
for i in range(n):
    txt= sys.stdin.readline().strip()
    arr.append(txt)

for element in arr:
    for i in range(len(element)):
        num = 10**(len(element)-i-1)
        det[element[i]] +=num
for value in det.values():
    if value > 0:
        ans_arr.append(value)
ans_arr = sorted(ans_arr,reverse=True)
for i in range(len(ans_arr)):
    ret += ans_arr[i]*(9-i)

print(ret)