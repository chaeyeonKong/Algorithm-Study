def solution(topping):
    cnt=0
    
    dict = {}
    left = set()
    for el in topping:
        if el in dict:
            dict[el]+=1
        else:
            dict[el]=1
    
    for el in topping:
        left.add(el)
        if el in dict:
            if dict[el]==1:
                del(dict[el])
            else:
                dict[el]-=1
        if len(left) == len(dict):
            cnt+=1
            
    
    return cnt
