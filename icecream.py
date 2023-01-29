n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=0
def dfs(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                dfs(nx,ny)
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            graph[i][j]=1
            dfs(i,j)
            print(graph)
            count+=1
print(graph)
print(count)