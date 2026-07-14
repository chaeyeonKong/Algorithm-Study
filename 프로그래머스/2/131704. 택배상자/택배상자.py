from collections import deque

def solution(order):
    
    arr = deque([0 for i in range(len(order))])
    
    cnt=1
    for el in order:
        arr[el-1] = cnt
        cnt+=1
        
    su = 1
    ans=0
    s=[]
    
    while(True):
        check1=True; check2=True
        if arr!=deque([]):
            belt1 = arr.popleft()
            if belt1==su:
                ans+=1
                su+=1
            elif belt1 != su:
                s.append(belt1)
                check1=False
                continue
        else:
            check1=False
                
        if s!=[]:
            belt2 = s.pop()
            if belt2 != su:
                s.append(belt2)
                check2=False
            else:
                su+=1
                ans+=1
        else:
            check2=False
                
        if check1 == False and check2 == False:
            break
            
    return ans