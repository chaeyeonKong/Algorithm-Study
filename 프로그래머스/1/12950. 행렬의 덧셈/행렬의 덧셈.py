def solution(arr1, arr2):
    n = len(arr1)
    answer = []
    
    for i in range(n):
        
        li = []
        for j in range(len(arr1[i])):
            k = 0
            k+=arr1[i][j]
            k+=arr2[i][j]
            li.append(k)
        answer.append(li)
    return answer