A = list(input().upper())
word = dict.fromkeys(A,0)

for i in range(len(A)): word[A[i]]+=1

w_sort = sorted(word.values(),reverse=True)

if(len(A)==1):
    print(A[0])
elif(w_sort[0]==w_sort[1]):
    print("?")
else:
    result =[k for k, v in word.items() if v == w_sort[0]][0]
    print(result)


