from collections import deque
import heapq
def solution(maps):
    answer = 0
    #q=deque()
    min=987654321
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    n=len(maps)
    m=len(maps[0])
    q=[]
    heapq.heappush(q,(1,0,0))
    maps[0][0]=0
    while q:
        d,x,y=heapq.heappop(q)
        #print(d,x,y)
        if x==n-1 and y==m-1:
            if min>d:
                min=d
                break
        d+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<n and nx>=0 and ny<m and ny>=0:
                if maps[nx][ny]==1:
                    heapq.heappush(q,(d,nx,ny))
                    maps[nx][ny]=0
    #print(min)
    if min!=0:
        answer=min
    else:
        return -1
    #print(answer)
    return answer
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
