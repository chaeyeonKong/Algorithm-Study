



def solution(clothes):
    
    dict = {}
    
    for i in range(len(clothes)):
        target = clothes[i][1]
        if target not in dict:
            dict[target] = 2
        else:
            dict[target] += 1
    
    ans = 1
    for el in dict:
        ans*=dict.get(el)
    
    return ans-1