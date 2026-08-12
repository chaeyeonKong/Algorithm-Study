def solution(t, p):
    
    left = 0 
    right = len(p)
    answer = 0
    
    while(right<=len(t)):
        target = int(t[left:right])
        if target <= int(p):
            answer+=1
        left+=1
        right+=1
        
    return answer