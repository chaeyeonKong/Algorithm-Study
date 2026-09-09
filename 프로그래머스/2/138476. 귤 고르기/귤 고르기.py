def solution(k, arr):
    
    
    dict = {}
    
    for el in arr:
        if el in dict:
            dict[el] += 1
        else:
            dict[el] = 1
        
    li = []
    for el, em in dict.items():
        li.append((el,em))
    li = sorted(li, key=lambda x:-x[1])
    
    cnt = 0
    for i in range(len(li)):
        cnt+=1
        k-=li[i][1]
        if k<=0:
            return cnt
        
    return cnt
    # dict = sorted(dict, key=lambda x:x)
    # sorted(student_tuples, key=lambda student: student[2])   # sort by age

    
    
            