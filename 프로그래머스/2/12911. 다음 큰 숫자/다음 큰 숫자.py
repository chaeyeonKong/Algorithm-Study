def tran(n):
    su = []
    cnt = 0
    while(True):
        su.append(n%2)
        n = n//2
        if n<=1:
            su.append(n)
            break
    
    for el in su:
        if el==1:
            cnt+=1
    return cnt

def solution(n):
    answer = 0
    cnt = 0
    ans_cnt = tran(n)

    k = 0
    while(True):
        k+=1
        su = tran(n+k)
        if su==ans_cnt:
            answer = (n+k)
            break
            
    return answer