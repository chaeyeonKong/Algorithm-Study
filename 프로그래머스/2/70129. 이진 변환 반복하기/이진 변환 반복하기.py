def solution(s):
    answer = []
    cnt = 0
    n = 0 

    while s!="1":
        cnt+=s.count("0")
        s = s.replace("0","")        
        s = bin(len(s))[2:] # 0b 제거하기 위해 [2:0] 하는 것        
        n+=1
        
    answer.append(n)
    answer.append(cnt)
    
    return answer