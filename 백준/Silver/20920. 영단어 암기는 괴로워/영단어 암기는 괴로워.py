import sys
n, k = map(int, sys.stdin.readline().strip().split())
dict = {}
for i in range(n):
    word = str(sys.stdin.readline().strip())
    if len(word)>=k:
        if word not in dict:
            dict[word] = int(1)
        else:
            dict[word]+=1

dict = sorted(dict, key=lambda x:(-dict[x], -len(x), x))
# dict = sorted(dict, key=lambda x:(x[1],len(x[0])))
for el in dict:
    print(el)