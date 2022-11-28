import sys
input = sys.stdin.readline
hap=0
for i in range(5):
    k = int(input())
    if k<40:
        k=40
    hap+=k
print(hap//5)

#dp 개념 공부하기용 떼우는 문제