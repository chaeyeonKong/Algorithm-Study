
def solution(brown, yellow):
    n = brown + yellow 
    s = []
    answer = [0,0]
    for i in range(2,(n//2)+1):
        if n%i==0:
            s.append(i)
    
    s.sort(reverse=True)
    
    print(s)
    for i in range((len(s)//2)+1):
        b=0
        y=0 
        left= i
        right = len(s)-1-i
        
        b += s[left]*2 # 가로 가장자리
        if 3<=s[right]: # 세로 가장자리
            b+=(s[right]-2)*2
                
        y = n-b
        if b==brown and y==yellow:
            return [s[left], s[right]]
        
    if answer==[0,0] and len(s)==1:
        answer = [s[0],s[0]]
        
    return answer
    