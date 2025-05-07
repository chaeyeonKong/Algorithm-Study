def solution(n):
    answer = 1
    
    for i in range(1,n+1):
        k = i
        for j in range(i+1,n+1):
            k+=j
            print(k)
            if k==n:
                answer+=1
                break
            if k>n:
                break
                
    
    return answer