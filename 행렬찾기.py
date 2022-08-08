T=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    global resultx,resulty,n
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n and arr[nx][ny]!=0:
            if nx*ny>=resultx*resulty:
                resultx=nx
                resulty=ny
            arr[nx][ny]=0
            dfs(nx,ny)
    return
for test_case in range(1,T+1):
    n=int(input())
    arr=[]
    answer=[]
    time=0
    for i in range(n):
        arr.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            resultx=0
            resulty=0
            if arr[i][j]!=0:
                arr[i][j]=0
                time+=1
                dfs(i,j)
                #print(i,j,resultx,resulty)
                answer.append((resultx-i+1,resulty-j+1))
    c=sorted(answer,key=lambda x : (x[0]*x[1],x[0]))
    print("#{} {}".format(test_case,time),end=" ")
    for i in c:
        for j in i:
            print(j,end=" ")
    print()