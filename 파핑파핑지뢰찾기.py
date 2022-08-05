T=int(input())
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
def dfs(x,y):
    global time,n
    print(visited)
    k=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny]==0 and map[nx][ny]=='*':
            k=1
    if k==0:
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny]==0:
                visited[nx][ny]=1
                dfs(nx,ny)
    return
for test_case in range(1,T+1):
    n=int(input())
    map=[[] for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        map[i]=list(input())
    print(map)
    print(visited)
    time=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and map[i][j]=='.':
                visited[i][j]=1
                time+=1
                dfs(i,j)
            elif map[i][j]=='*':
                visited[i][j]=2
    #print(visited)
    print("#{} {}".format(test_case,time))
