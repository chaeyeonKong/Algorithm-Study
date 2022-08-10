import sys,collections
input = sys.stdin.readline
N = int(input())
arr = collections.deque(i+1 for i in range(N))
# print(arr)
for i in range(N-1):
    arr.popleft()
    arr.append(arr[0])
    arr.popleft()
    # print(arr)
print(arr[0])