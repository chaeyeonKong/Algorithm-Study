import math
 
def solution(n, words):
    answer = [0,0]
    dict = {}
    dict[words[0]]=1
    for i in range(1,len(words)):
        before = words[i-1][-1]
        target = words[i]
        if target[0] == before:
            if target not in dict:
                dict[target] = 1
            else:
                 # math.ceil(((i+1)/n))
                print(i+1, n)
                answer = [(i%n)+1, math.ceil((i+1)/n)]
                return answer
        else:
             # math.ceil(((i+1)/n))
            answer = [(i%n)+1,math.ceil((i+1)/n)]
            return answer

    return answer