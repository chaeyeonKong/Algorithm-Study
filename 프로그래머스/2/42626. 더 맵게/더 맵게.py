import heapq

def solution(s, k):
    
    heapq.heapify(s)
    cnt=0
    
    while(True):
        if s[0] < k:
            if len(s)<2:
                return -1
            
            one = heapq.heappop(s)
            two = heapq.heappop(s)
            heapq.heappush(s,one+(two*2))
            
        else:
            break
        cnt+=1
        
        
    return cnt