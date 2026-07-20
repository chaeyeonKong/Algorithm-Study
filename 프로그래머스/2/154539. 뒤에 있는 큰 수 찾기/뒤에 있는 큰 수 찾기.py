def solution(numbers):

    ans = [-1] * len(numbers)
    s =[]
    
    for i in range(len(numbers)):
        
        while s and numbers[s[-1]]< numbers[i]:
            idx = s.pop()
            ans[idx] = numbers[i]
        
        s.append(i)
    
        
    return ans