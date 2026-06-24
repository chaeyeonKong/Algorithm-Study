def solution(n, times):

    end = min(times) * n
    start = 1
    
    cnt = 0
    answer = 0
    while(start <= end):
        mid = (start + end) // 2
        
        cnt = 0
        answer = 0
        for t in times:
            cnt += mid//t
            
        if cnt<n:
            start=mid+1
        else:
            end=mid-1
    print(start, end ,mid )
    return start