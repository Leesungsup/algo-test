from collections import deque
n=9
mine=[]
def bfs(x,y):
    q=deque()
    q.append([x,y])
    check[x][y]=1
    while q:
        x,y=q.popleft()
        count=0
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<n:
                if mine[nx][ny]==1:
                    count+=1
        minecount[x][y]=count
        if count>0:
            continue
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<n:
                if check[nx][ny]==0 and mine[nx][ny]==0:
                    check[nx][ny]=1
                    q.append([nx,ny])
for i in range(n):
    mine.append(list(map(int,input().split())))
x,y=map(int,input().split())
dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,1,-1]
check=[[0]*x for y in range(n)]
minecount=[[0]*x for y in range(n)]
if mine[x-1][y-1]==1:
    check[x-1][y-1]=1
    minecount[x-1][y-1]=-1
else:
    bfs(x-1,y-1)
for i in range(n):
    for j in range(n):
        if check[i][j]==1:
            print(minecount[i][j],end='')
        else:
            print('_',end=' ')
    print()
