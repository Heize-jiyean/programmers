def solution(n):
    
    res=[[0]*i for i in range(1,n+1)]#배열 res
    y=-1 #좌표값 x,y
    x=0
    num=1
    
    for i in range(n):
        for j in range(i,n):
            angle=i%3 # 나머지 0,1,2
            
            if angle==0:
                y+=1
            elif angle==1:
                x+=1
            elif angle==2:
                y-=1
                x-=1
                
            res[y][x] = num
            num+=1
    

    return [i for j in res for i in j]