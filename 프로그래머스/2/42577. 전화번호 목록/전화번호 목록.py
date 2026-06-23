from collections import deque

def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        target = phone_book[i]
        el = phone_book[i+1]
        if target==el[:len(target)]:
            return False
            
    return True
