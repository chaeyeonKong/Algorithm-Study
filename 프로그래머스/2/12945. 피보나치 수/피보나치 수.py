def solution(n):
    if n == 0:
        return 0
    elif n == 1: 
        return 1 


def fibo(n):
    if n<=1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a+b 
    return b % 1234567

def solution(n):
    
    answer = fibo(n)
    return answer