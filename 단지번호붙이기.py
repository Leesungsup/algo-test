n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=1
def dfs(x,y,count):
    global dan
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny]==1:
                graph[nx][ny]=count
                dan+=1
                dfs(nx,ny,count)

for i in range(n):
    for j in range(n):
        dan=0
        if graph[i][j]==1:
            count+=1
            dan+=1
            graph[i][j]=count
            dfs(i,j,count)
            # print(graph)
            print(dan)
print(graph)
print(count-1)