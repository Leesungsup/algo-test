from collections import deque
T=int(input())
for test_case in range(1,T+1):
    a,b=map(int,input().split())
    arr=[[0]*i for i in range(100)]
    k=1
    q=deque()
    for i in range(100):
        for j in range(len(arr[i])):
            if k==a:
                arr[i][j]=k
                q.append((i,j,0,k))
            arr[i][j]=k
            k+=1
        if k>max(a,b):
            height=i
            break
    dx=[-1,1,0,0,-1,1]
    dy=[0,0,1,-1,-1,1]
    while q:
        x,y,dist,k=q.popleft()
        if k==b:
            break
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=1 and nx<=height and ny>=0 and ny<len(arr[nx]):
                if arr[nx][ny]!=0:
                    q.append((nx,ny,dist+1,arr[nx][ny]))
                    arr[nx][ny]=0
    print("#{} {}".format(test_case,dist))
