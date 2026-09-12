def solution(numbers):
    arr = list(map(str,numbers))
    arr.sort(key=lambda x:x*3, reverse=True)
    answer = str(''.join(arr))
    if answer[0]=='0':
        return '0'
    else: return answer
