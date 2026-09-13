from collections import deque
def solution(arr):
    q = deque(list(map(int,str(arr))))
    answer = 0
    while(q):
        k = q.pop()
        if k!=0:
            if k < 5:
                answer += k
            elif k>5:
                answer += (10-k)
                if q:
                    q[-1]+=1
                else:
                    answer+=1
            elif k==5:
                answer+=5
                if q and q[-1]>=5: 
                    q[-1]+=1
            
    return answer