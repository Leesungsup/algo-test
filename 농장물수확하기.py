from collections import deque
T=int(input())
for i in range(1,T+1):
    graph=[]
    q=deque()
    sum=0
    n=int(input())
    ma=[[0]*n for _ in range(n)]
    print(ma)
    for j in range(n):
        graph.append(list(map(int,input())))
    print(graph)
    x=n//2
    y=n//2
    sum+=graph[x][y]
    ma[x][y]=1
    q.append((x,y,0))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while q:
        x,y,num=q.popleft()
        if num==n//2:
            continue
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<n and ma[nx][ny]==0:
                sum+=graph[nx][ny]
                ma[nx][ny]=1
                q.append((nx,ny,num+1))
    print("#{} {}".format(i,sum))
