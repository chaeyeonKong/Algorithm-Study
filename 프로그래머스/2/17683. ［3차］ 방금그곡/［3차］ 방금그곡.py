def solution(m, musicinfos):
    answer = ''

    ans = []
    for i in range(len(musicinfos)):
        arr = ''

        t1, t2, song, code = map(str, musicinfos[i].split(","))

        last_hour, last_min = map(int, t2.split(":"))
        first_hour, first_min = map(int, t1.split(":"))

        play_time = ((last_hour - first_hour) * 60) + abs(last_min - first_min)  # 음악 실행 시간

        idx = 0
        cnt = 0
        shop = 0
        while (True):
            arr += code[idx]
            cnt += 1
            idx += 1

            if idx >= len(code):
                idx = 0

            if code[idx] == '#':
                play_time += 1
                shop+=1

            if cnt >= play_time: break

        
        print(m, arr)

        f_idx = 0
        while (True):
            target = arr.find(m,f_idx)
            if target ==-1:
                break
                
            f_idx = target+len(m)
            if f_idx == len(arr) or arr[f_idx]!='#': # 끝까지 같거나, k가 #이 아니면
                ans.append([song, play_time - shop])
            
        
    ans.sort(key=lambda x: -x[1])
    if ans==[]:
        answer = '(None)'
    else:
        answer = ans[0][0]
    print(ans)
    
    return answer