import sys
input = sys.stdin.readline
x,y,w,s= map(int,input()[:-1].split())

d = x+y

ret1 = d*w #평행으로만

if d%2==0:
    ret2 = max(x,y)*s #대각선으로만
else:
    ret2 = (max(x,y)-1)*s+w #홀수일 때는 나누어 떨어지지 않으므로 대각선으로 최대한 이동하고 남은 1회는 평행이동
ret3 = (min(x,y)*s)+(abs(x-y)*w) #대각선 + 평행 (min(x,y)를 찾아서 대각선으로 갈 수 있는 값을 찾고, 나머지 평행이동)

print(min(ret1,ret2,ret3))
