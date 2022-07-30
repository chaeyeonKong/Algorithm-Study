N = int(input())
score = map(int,list(input().split()))

score_sort = sorted(score)
print("%d %d"%(score_sort[0],score_sort[N-1]))