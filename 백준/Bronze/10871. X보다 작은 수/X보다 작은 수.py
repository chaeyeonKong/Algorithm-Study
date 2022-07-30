N, X = map(int,input().split())
Nlist = list(input().split())
result = ""
for i in range(N):
    if int(Nlist[i]) < X:
        result += Nlist[i] + " "
print(result)
