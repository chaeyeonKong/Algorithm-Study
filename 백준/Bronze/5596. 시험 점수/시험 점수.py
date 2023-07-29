import sys
arr1 = sys.stdin.readline()[:-1].split()
arr2 = sys.stdin.readline()[:-1].split()
hap1=0; hap2=0
for i in range(4):
    hap1 += int(arr1[i])
    hap2 += int(arr2[i])
if hap1>=hap2: print(hap1)
else: print(hap2)