

def solution(order):
        
    s = []
    k = 1
    ans = 0
    
    for target in order:
        while k < target:
            s.append(k)
            k+=1
        
        if k == target:
            ans +=1
            k+=1
        elif s and s[-1]==target:
            s.pop()
            ans+=1
        else:
            break
            
    return ans