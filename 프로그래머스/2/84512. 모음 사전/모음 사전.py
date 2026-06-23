def solution(word):
    
    arr = ['A','E','I','O','U']
    
    answer = 0
    cnt = 0
    Flag=True
    def dfs(target):
        nonlocal cnt, Flag, answer
        if Flag:
            if target == word:
                Flag=False
                answer = cnt
                return True

            if len(target)==5:
                return False

            for ch in arr:
                cnt+=1
                dfs(target+ch)
    
    dfs("")
    return answer