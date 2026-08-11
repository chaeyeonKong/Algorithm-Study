from collections import deque
def solution(skill, skill_trees):
    cnt = 0
    for i in range(len(skill_trees)):
        sk = deque(skill)
        target = skill_trees[i]
        check=True
        s = set(sk)
        for el in target:
            if el in s:
                if el != sk.popleft():
                    check=False
                    break
        if check:
            cnt+=1
        
    return cnt