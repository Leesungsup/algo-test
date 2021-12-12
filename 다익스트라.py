import heapq
import sys
INF=int(1e9)
n,m=map(int,input().split())
start=int(input())
distance=[INF]*(n+1)
map=[[] for _ in range(n+1)]
for i in range(n+1):
    a,b,c=map(int,sys.stdin.readline().split())
    map[a].append((b,c))
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in map[now]:
            if distance[i[0]]>dist+i[1]:
                distance[i[0]]=dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))
dijkstra(start)
print(distance)
import heapq
import sys
INF=int(1e9)
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance = [INF]*(n+1)
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
start=int(input())
def dijkstra(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            if distance[i[1]]<dist+i[0]:
                distance[i[1]]=dist+i[0]
                heapq.heappush(q,(dist+i[0],i[1]))
import heapq
from collections import deque
def BackTracking(maze,ex,ey):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    foots=[]
    foots.append([ex,ey])
    foot = maze[ex][ey]
    while(True):
        for di in range(0,4):
            x = ex + dx[di]
            y = ey + dy[di]
            if(maze[x][y] == foot-1):
                foots.append([x,y])
                ex = x
                ey = y
                foot = maze[x][y]
                break
        if(foot == 1):
            foots.reverse()
            return foots
def dijkstra(x,y,ex,ey):
    q=[]
    x1=x
    y1=y
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    map1 = [[-1] * len(map[n-1]) for _ in range(n)]
    map1[x][y]=0
    heapq.heappush(q,(1,(x,y)))
    list=[]
    list=deque()
    while True:
        dist,(x,y)=heapq.heappop(q)
        list.append((x,y))
        if map[x][y]==3:
            break
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx< n and 0<= yy < len(map[n-1]) and map1[xx][yy] < 0:
                if map[xx][yy]==0 or map[xx][yy]==3:
                    map1[xx][yy]=dist
                    heapq.heappush(q,(dist+1,(xx,yy)))
    route=BackTracking(map1,ex,ey)
    route.append((ex,ey))
    for i in route:
        print(i[1],i[0])
    return