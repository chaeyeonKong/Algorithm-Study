import sys
x,y = map(int,sys.stdin.readline().split())
z = y*100//x

start = 1
end = x
ans = -1

while(start <= end):
    mid = (start+end)//2
    k = (y+mid)*100 // (x+mid)

    if k>z:
        ans = mid
        end = mid-1
    else:
        start = mid+1

print(ans)