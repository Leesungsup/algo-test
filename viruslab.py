n,m=map(int,input().split())
graph=[]
temp=[[0]*m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int,input().split())))
count=0
result=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)
def get_score():
    c=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                c+=1
    return c

def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        result=max(result,get_score())
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j]==0:
                    graph[i][j]=1;
                    count+=1
                    dfs(count)
                    graph[i][j]=0
                    count-=1
dfs(0)

print(result)
#x축 y축 조심할 것! append제외하고 리스트 컴프리션 필요!
