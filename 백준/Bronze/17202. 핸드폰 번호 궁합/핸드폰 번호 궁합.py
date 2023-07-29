import sys
input1 = list(sys.stdin.readline()[:-1])
input2 = str(sys.stdin.readline()[:-1])
ret=[]
result=[]
for i in range(8):
    ret.append(int(input1[i]))
    ret.append(int(input2[i]))

i=1
while(True):
    result.append((ret[i]+ ret[i-1])%10)
    i += 1
    if i>=len(ret):
        if len(result)<=2:
            print(str(result[0])+str(result[1]))
            break
        else:
            ret=[]
            ret = result
            result=[]
            i = 1