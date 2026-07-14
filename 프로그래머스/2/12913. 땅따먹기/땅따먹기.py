def solution(land):
    
    x = len(land)
    y = len(land[0])
    
    
    for i in range(1,x):
        
        for j in range(y):
            li=[]
            for k in range(y):
                if k!=j:
                    li.append( land[i][j]+land[i-1][k])
            land[i][j] = max(li)
    return max(land[x-1])
    