from collections import deque


def solution(priorities, location):
    q = deque(priorities)
    idxq = deque([i for i in range(len(priorities))])    
    cnt=0
    
    while(True):
        k = max(q)
        #print(k, q, idxq)
        
        
        idx = idxq.popleft()
        target = q.popleft()
        
        
        if target==k:
            cnt+=1
            if idx==location:
                return cnt; 
        else:
            idxq.append(idx)
            q.append(target)
            
        #print(k, q, idxq)
        #print("-------")
        
    return cnt