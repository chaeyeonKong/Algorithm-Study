from collections import deque

def solution(progresses, speeds):
    
    q = deque(progresses)
    speeds = deque(speeds)
    cnt=0
    answer = []
    while(q):
        if q[0]>=100:
            cnt+=1
            q.popleft()
            speeds.popleft()
        else:
            if cnt>0:
                answer.append(cnt)
            cnt=0
            for i in range(len(q)):
                q[i] += speeds[i]
    if cnt>0:
        answer.append(cnt)

    return answer