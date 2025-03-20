import sys
n = int(sys.stdin.readline().strip())
arr  = []
dict = {}

for i in range(n):
    k =int(sys.stdin.readline().strip())

    if k in dict:
        dict[k]+=1
    else:
        dict[k] = 1

if len(dict)==1:
    print(k)
else:
    dict = sorted(dict.items(), key=lambda x:(-x[1],x[0]))
    print(dict[0][0])