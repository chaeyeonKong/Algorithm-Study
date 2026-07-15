

def solution(s):
    
    k=""
    before=""
    arr=[]
    for target in s:
        if target=="{":
            li=[]
            before="{"
            
        elif target==",":
            if k!="":
                li.append(int(k))
                k=""
            before=","
        
        elif target=="}":
            if k!="" and before!="}":
                li.append(int(k))
                arr.append(li)
            k=""
            before="}"
            
        else:
            k+=target
    
    # 정제 완료 -----
    
    arr = sorted(arr, key=lambda x:len(x))
    
    ret = []
    ret.append(arr[0][0])
    for i in range(1,len(arr)):
        for el in ret:
            if el in arr[i]:
                arr[i].remove(el)
        ret.append(arr[i][0])

    return ret