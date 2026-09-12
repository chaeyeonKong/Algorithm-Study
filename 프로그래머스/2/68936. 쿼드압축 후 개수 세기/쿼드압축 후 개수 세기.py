def solution(arr):
    
    n = len(arr)
    
    answer = [0,0]
    
    def qu(x, y, length):
        
        val = arr[x][y]
        for i in range(x, x+length):
            for j in range(y, y+length):
                if arr[i][j]!=val:
                    half = length//2
                    qu(x, y, half)
                    qu(x+half, y, half)
                    qu(x, y+half, half)
                    qu(x+half, y+half, half)
                    return
                
        answer[val]+=1
    qu(0,0,n)
             
    return answer