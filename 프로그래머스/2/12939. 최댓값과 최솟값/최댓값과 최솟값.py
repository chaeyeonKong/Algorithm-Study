def solution(s):
    arr= list(map(int, s.split()))
    print(str(min(arr)),str(max(arr)))
    answer = str(min(arr))
    answer = answer + " " +str(max(arr))
    
    return answer