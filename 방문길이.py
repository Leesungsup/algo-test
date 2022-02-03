from collections import deque
def solution(dirs):
    answer = 0
    map=[[0]*11 for _ in range(11)]
    map[5][5]=1
    y=5
    x=5
    sum=0
    for i in dirs:
        if i=='U':
            if y-1>=0 and y<11:
                if map[y-1][x]==0:
                    sum+=1
                    y-=1
                    map[y][x]=1
                else:
                    y-=1
        elif i=='D':
            if y>=0 and y+1<11:
                if map[y+1][x]==0:
                    sum+=1
                    y+=1
                    map[y][x]=1
                else:
                    y+=1
        elif i=='R':
            if x>=0 and x+1<11:
                if map[y][x+1]==0:
                    sum+=1
                    x+=1
                    map[y][x]=1
                else:
                    x+=1
        elif i=='L':
            if x-1>=0 and x<11:
                if map[y][x-1]==0:
                    sum+=1
                    x-=1
                    map[y][x]=1
                else:
                    x-=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    x=5
    y=5
    q=deque()
    q.append((5,5))
    while q:
        y,x=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if map[ny][nx]==1 and 0<=nx<11 and 0<=ny<11 and map[y][x]==1:
                map[y][x]=0
                q.append((ny,nx))
                answer+=1
    print(answer)
    return answer
solution("ULURRDLLU")
def solution1(dirs):
    answer=0
    d={'U':(0,-1),'D':(0,1),'R':(1,0),'L':(-1,0)}
    x=0
    y=0
    route=set()
    for i in dirs:
        nx=x+d[i][0]
        ny=y+d[i][1]
        if nx>=-5 and nx<=5 and ny>=-5 and ny<=5:
            route.append((x,y,nx,ny))
            route.append((nx,ny,x,y))
            x=nx
            y=ny
    print(len(route))
    return len(route)//2