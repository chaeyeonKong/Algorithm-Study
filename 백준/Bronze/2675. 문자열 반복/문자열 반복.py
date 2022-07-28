
N = int(input())
result = ""
for i in range(N):
    K,str = input().split()
    str = list(str)
    for j in range(len(str)):
        for k in range(int(K)):
            result += str[j]
    print(result)
    result = ""

