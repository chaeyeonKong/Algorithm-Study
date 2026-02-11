
def solution(k, tangerine):
    
    dict = {}
    n = len(tangerine)
    for i in range(n):
        if tangerine[i] in dict:
            dict[tangerine[i]] +=1
        else:
            dict[tangerine[i]]=1
        
    b = sorted(dict.items(), key=lambda x:x[1])
    
    for i in range(len(b)):
        if n==k:
            break
        for j in range(b[i][1]):
            if n==k:
                break
            dict[b[i][0]]-=1
            n-=1
            
    cnt = 0
    for i in range(len(b)):
        if dict[b[i][0]]!=0:
            cnt+=1
    
    print(cnt)
    
    return cnt