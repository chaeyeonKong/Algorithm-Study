N = int(input())
score = [0]*N
hap = 0; total = 0;

for i in range(N):

    total = 0
    score[i] = input()
    for j in range(len(score[i])):
        if score[i][j] == 'O':
            hap+=1
        else:
            hap = 0

        total+=hap
    hap = 0
    print(total)