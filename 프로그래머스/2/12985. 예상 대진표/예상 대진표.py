def solution(n,a,b):
    arr = [i+1 for i in range(n)]
    arr[a-1] = 'A'
    arr[b-1] = 'B'
    level = 0
    while(len(arr)>1):
        level+=1
        li = []
        for i in range(0,len(arr),2):
            if arr[i]=='A' or arr[i+1]=='A':
                if arr[i+1]=='B' or arr[i]=='B':
                    return level
                li.append('A')
            elif arr[i+1]=='B' or arr[i]=='B':
                if arr[i+1]=='A' or arr[i]=='A':
                    return level
                li.append('B')
            else:
                li.append(arr[i])
            
        arr = li
        
    return level