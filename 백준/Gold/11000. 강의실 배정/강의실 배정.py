# 강의실 배정

import sys
import heapq
n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr = sorted(arr, key=lambda x:(x[0],x[1]))


room = []
heapq.heappush(room, arr[0][1])

for i in range(1,n):
    if room[0] <= arr[i][0]:
        heapq.heappop(room)
    heapq.heappush(room,arr[i][1])


print(len(room))