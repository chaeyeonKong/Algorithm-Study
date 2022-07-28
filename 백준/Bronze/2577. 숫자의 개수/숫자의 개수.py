a = int(input())
b = int(input())
c = int(input())
K = list(str(a*b*c))

dict={}
for i in range(10):
    dict[i] = 0

for i in range(len(K)):
    dict[int(K[i])] += 1

for i in range(len(dict)):
    print(dict[i])