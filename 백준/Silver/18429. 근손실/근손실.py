import sys
n,k = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
li = []
cnt = 0
visited = [False for _ in range(n)]
def bfs(li):
    ret = 0
    for i in range(n):
        ret+=(li[i]-k)
        if ret<0:
            return False
    return True

def back(li):
    global cnt

    if len(li)==n:
        if bfs(li):
            cnt+=1
        return

    for i in range(n):
        if not visited[i]:
            li.append(arr[i])
            visited[i] = True
            back(li)
            li.pop()
            visited[i] = False
back([])
print(cnt)