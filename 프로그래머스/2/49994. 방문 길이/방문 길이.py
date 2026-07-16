def solution(arr):
    # arr = "RRRRRRRRRRDDDDDDUUUU"
    x=0; y=0
    dict={"U":(1,0), "D":(-1,0),"R":(0,1),"L":(0,-1)}
    visited=[]
    for i in range(len(arr)):
        target = dict[arr[i]]
        if -5<=x+target[0]<=5 and -5 <= y+target[1] <=5:
            if (x,y,x+target[0],y+target[1] ) not in visited:
                visited.append((x,y,x+target[0],y+target[1]))
                visited.append((x+target[0],y+target[1],x,y))
            # else:
            #     print("존재한다", x,y,x+target[0],y+target[1] )
            x+=target[0]
            y+=target[1]
    # print("ans=",len(visited), " " ,visited)
            
    return len(visited)/2