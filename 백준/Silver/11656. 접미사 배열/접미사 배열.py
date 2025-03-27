import sys
word = str(sys.stdin.readline().strip())
arr= []
idx = 0
while(True):
    arr.append(word[idx:len(word)])
    idx+=1
    if idx>=len(word):break
arr.sort()
for el in arr:
    print(el)