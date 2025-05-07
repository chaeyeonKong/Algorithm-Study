from collections import deque
arr = deque()
ans = deque()

def solution(s):
    
    for el in s:
        if el=="(":
            ans.append("(")
        else:
            if ans!=deque([]):
                ans.pop()
            else:
                return False
            
    if ans==deque([]):
        return True
    else:
        return False
#     cnt=0
#     answer = True
#     len(s)
#     for i in range(len(s)):
#         arr.append(s[i])
    
#     if arr[-1]=="(":
#         return False
#     else:
#         for i in range(len(s)):
#             if arr[i]=="(":
#                 ans.append("(")
#             else:
#                 ans.pop()
#         if ans==deque([]):
#             return True
#         else:
#             return False
        
                