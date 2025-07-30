# 회의실 배정
import sys

n = int(sys.stdin.readline().strip())
time=[]
for _ in range(n):
    time.append(tuple(map(int, sys.stdin.readline().split())))

time.sort(key=lambda x:(x[1],x[0]))

cnt=0
endtime = 0
ret = 0
for start, end in time:
    if start>=endtime:
        cnt+=1
        endtime = end
    if ret<cnt:
        ret = cnt
print(ret)
