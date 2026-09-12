from collections import deque

def solution(q1, q2):
    
    q1 = deque(q1)
    q2 = deque(q2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    cnt=0
    
    while(q1 and q2 and cnt<300000):
        if sum1==sum2:
            return cnt
        elif sum1<sum2:
            k = q2.popleft()
            q1.append(k)
            sum1+=k
            sum2-=k
        elif sum1>sum2:
            k = q1.popleft()
            q2.append(k)
            sum2+=k
            sum1-=k
        cnt+=1
        
        
    return -1