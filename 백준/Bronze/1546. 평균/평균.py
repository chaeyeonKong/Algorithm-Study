num = int(input())
score = input().split()
M = max([int(i) for i in score])

result = 0

for i in range(len(score)):
    result += (int(score[i])/int(M))*100

print(result/num)

