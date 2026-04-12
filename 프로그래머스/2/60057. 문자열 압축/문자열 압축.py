def solution(s):
    
    ret = len(s)
    for i in range(1,len(s)):
        target = s[:i]
        idx = i
        result = 1
        ans = ""
        for j in range(idx, len(s), idx):
            if target == s[j:j+idx]:
                result+=1
            else:
                if result>1:
                    ans+=str(result)
                ans+=target
                result = 1
                target = s[j:j+idx]
        if result>1:
            ans+=str(result)
        ans+=target
        
        if ans!="":
            if ret > len(ans):
                ret = len(ans)
            
    return ret