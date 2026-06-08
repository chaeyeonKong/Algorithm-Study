def solution(want, number, discount):
    answer = 0
    origin_dict={}
    for i in range(len(want)):
        origin_dict[want[i]] = number[i]
    
    
    for i in range(len(discount)-9):
        dict = origin_dict.copy()
        # print("origin_dict",origin_dict)
        
        
        cnt = 0
        for j in range(i,i+10):
            if discount[j] in dict:
                dict[discount[j]]-=1
                if dict[discount[j]]==0:
                    cnt+=1
                    
        # print("       dict",dict)      
        # print(cnt, len(dict))
        if cnt==len(dict):
            answer +=1
    
    return answer