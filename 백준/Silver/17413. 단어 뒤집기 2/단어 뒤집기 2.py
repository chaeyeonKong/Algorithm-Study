import sys
txt = sys.stdin.readline().strip()
ans = ""
tag = 0
stack = []


for el in txt:
    if el == "<":
        if stack:
            while stack:
                ans += stack.pop()
        ans+=el
        tag = 1
        continue
    elif el == ">":
        ans += el
        tag = 0
        continue
    if tag==1:
        ans += el
    else:
        if el== " ":
            if stack:
                while stack:
                    ans += stack.pop()
            ans+=" "
        else:
            stack.append(el)


if stack:
    while stack:
        ans += stack.pop()


print(ans.lstrip())