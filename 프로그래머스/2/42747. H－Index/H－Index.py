def solution(arr):
    
    arr = sorted(arr)
    ans = 0
    
    for target in range(arr[-1]+1):
        cnt=0
        for i in range(len(arr)):
            if target <= arr[i]:
                cnt+=1
                
        if target<=cnt:
            ans=target
        
    return ans