import sys
a = []

while True:
    b = sys.stdin.readline().strip()
    if not b:
        break
    a.append(b)

for i in range(len(a)):
    no = 0
    if (int(a[i][0])==0):
        continue
    for j in range(len(a[i])//2):
        if a[i][j] != a[i][len(a[i])-(j+1)]:
            no+=1

    if no ==0:
        print("yes")
    else:
        print("no")