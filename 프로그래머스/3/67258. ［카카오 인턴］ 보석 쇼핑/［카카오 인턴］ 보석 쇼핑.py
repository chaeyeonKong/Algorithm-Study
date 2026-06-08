def solution(gems):
    kinds = len(set(gems))

    start = 0
    answer = len(gems)-1
    
    ans_start = 0
    ans_end = len(gems)-1
    
    
    dict = {}

    for end in range(len(gems)):
        gem = gems[end]

        if gem in dict:
            dict[gem] += 1
        else:
            dict[gem] = 1
        
        while kinds == len(dict):

            gem = gems[start]

            if dict[gem] > 1:
                dict[gem] -= 1
                start += 1
            else:
                if end - start < ans_end - ans_start:
                    ans_start = start
                    ans_end = end
                break
            
    return [ans_start+1, ans_end+1]