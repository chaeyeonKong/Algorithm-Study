def check(s):
    is_stack = False
    stack=[]
    while(s):
        target = s.pop()
        if target==")":
            stack.append('(')
        elif target=="}":
            stack.append('{')
        elif target=="]":
            stack.append('[')
        else:
            if stack:
                compare = stack.pop()
                if compare == target:
                    is_stack = True
                else:
                    is_stack=False
                    break
            else:
                is_stack=False
                break
    return is_stack
                
        
            
            
    
def solution(s):
    ans = 0
    origin_s = s
    if check(list(s))==True:
        ans+=1
    s = s[1:] + s[0]
    if check(list(s))==True:
        ans+=1
    while(True):
        s = s[1:] + s[0]
        if origin_s==s:break
        if check(list(s))==True:
            ans+=1        
    
    return ans