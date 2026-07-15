def solution(prices):
    
    arr = [0 for _ in range(len(prices))]
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                arr[i]+=1
            else:
                if i != len(prices)-1:
                    arr[i]+=1
                break

    return arr