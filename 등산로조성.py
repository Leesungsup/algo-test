from collections import deque
T=int(input())
def dfs(x,y,k,t,count):
    global n,answer
    if count>answer:
        answer=count
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        for j in range(k+1):
            if 0<=nx<n and 0<=ny<n and arr[x][y]>arr[nx][ny]-j and check[nx][ny]==0:
                if j!=0 and t==1:
                    temp=arr[nx][ny]
                    arr[nx][ny]=arr[nx][ny]-j
                    check[nx][ny]=1
                    dfs(nx,ny,k,0,count+1)
                    check[nx][ny]=0
                    arr[nx][ny]=temp
                else:
                    check[nx][ny]=1
                    dfs(nx,ny,k,1,count+1)
                    check[nx][ny]=0
for test_case in range(1,T+1):
    n,k=map(int,input().split())
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    arr=[]
    check=[[0]*n for _ in range(n)]
    answer=0
    for i in range(n):
        arr.append(list(map(int,input().split())))
    max_arr = []
    for i in range(n):
        max_arr.append(max(arr[i]))
    maxx = max(max_arr)
    #print(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=maxx:
                continue
            check[i][j]=1
            dfs(i,j,k,1,1)
            check[i][j]=0
    print("#{} {}".format(test_case,answer))
