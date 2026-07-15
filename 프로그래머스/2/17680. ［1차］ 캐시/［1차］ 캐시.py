from collections import deque
def solution(cacheSize, cities):
    
    q = deque([])
    cnt=0
    
    if cacheSize!=0:
        for i in range(len(cities)):
            target = cities[i].upper() # 대문자화
            if target not in q: # queue에 없음
                if len(q)==cacheSize: # 사이즈는 다 참
                    if q!=deque([]):
                        q.popleft()
                q.append(target)
                cnt+=5

            else: # queue에 있음
                q.remove(target) # 있는것 지우고
                q.append(target) # 다시 오른쪽 끝으로
                cnt+=1
    else:
        cnt = 5*len(cities)        
    return cnt
    
    