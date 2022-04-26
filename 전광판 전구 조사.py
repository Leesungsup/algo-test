from collections import deque
import copy
def bfs1(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph1[nx][ny]==0:
                graph1[nx][ny]=1
                q.append((nx,ny))
def bfs2(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph2[nx][ny]==1:
                graph2[nx][ny]=0
                q.append((nx,ny))
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
graph1=copy.deepcopy(graph)
graph2=copy.deepcopy(graph)
print(graph1)
print(graph2)
z=0
o=0
for i in range(n):
    for j in range(m):
        if graph2[i][j]==1:
            print(i,j)
            bfs2(i,j)
            o+=1
for i in range(n):
    for j in range(m):
        if graph1[i][j]==0:
            print(i,j)
            bfs1(i,j)
            z+=1

print(graph2)
print(z,o)