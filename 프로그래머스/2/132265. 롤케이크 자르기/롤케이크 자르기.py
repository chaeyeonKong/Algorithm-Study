def solution(topping):
    cnt=0
    dict={}
    li = set()
    for el in topping:
        if el in dict:
            dict[el]+=1
        else:
            dict[el]=1
    
    
    for i in range(len(topping)):
        target = topping[i]
        li.add(target)
        if dict[target]==1:
            del(dict[target])
        elif dict[target]>1:
            dict[target]-=1
            
        if len(li) == len(dict):
            cnt+=1
    
    return cnt
