def solution(prices):
    
    arr = [0] * len(prices)
    s=[]
    
#     for i:
#         while 스택맨위가격 > 현재가격:
#             idx = pop
#             arr[idx] = i - idx

#         push(i)

#     while s:
#         idx = s.pop()
#         arr[idx] = 마지막인덱스 - idx
        
    for i in range(len(prices)):
        cnt=0
        while s and prices[s[-1]] > prices[i]:
            idx = s.pop()
            arr[idx] = i - idx 
        
        s.append(i)

    while s:
        idx = s.pop()
        arr[idx] = len(prices)-(idx+1)
        

    return arr