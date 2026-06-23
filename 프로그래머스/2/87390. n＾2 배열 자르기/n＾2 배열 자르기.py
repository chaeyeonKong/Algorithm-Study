def solution(n, left, right):
        
    ret=[]
    
    for idx in range(left, right+1):
        row = idx // n
        col = idx % n
        ret.append(max(row,col)+1)
        
    return ret