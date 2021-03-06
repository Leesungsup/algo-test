from collections import deque
n,m=map(int,input().split())
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    graph.append(list(map(int,input())))
def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if graph[nx][ny]==1:
                    q.append((nx,ny))
                    graph[nx][ny]=graph[x][y]+1
bfs(0,0)
print(graph[n-1][m-1])
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
def dfs(x,y):
    if x>=n or x<0 or y>=m or y<0:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
count=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count+=1
print(count)
n,m,k,x=map(int,input().split())
d=[0]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(n):
    a,b=map(int,input().split())
    graph[a].append(b)
def bfs(x):
    q=[]
    q=deque()
    q.append(x)
    while q:
        x=q.popleft()
        for i in graph[x]:
            if d[i]==0:
                d[i]=d[x]+1
                q.append(i)
check=False
for i in range(n+1):
    if d[i]==k:
        check=True
        print(i,end='')
if check==False:
    print("-1")