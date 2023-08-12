import sys
a,b = map(int,sys.stdin.readline()[:-1].split())
arr=[]; darr=[]

for i in range(2,a+1):
    arr.append(i)

k=2; prime=0; check=0
while(check!=b and k<=a):
    if prime+k>a:
        k += 1
        prime=0
    else:
        prime+=k
        if prime in arr:
            arr.remove(prime)
            check += 1
            darr.append(prime)

if len(darr)+1<b:
    print(arr[b-len(darr)]-1)
else:
    print(prime)