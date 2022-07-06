T=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y,count,num):
    if count==7:
        #print(''.join(map(str,d)))
        answer.add(''.join(num))
        return
    num+=str(arr[x][y])
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 4>nx>=0 and 0<=ny<4:
            dfs(nx,ny,count+1,num)
for test_case in range(1,T+1):
    arr=[]
    answer=set()
    for i in range(4):
        arr.append(list(map(int,input().split())))
    for i in range(4):
        for j in range(4):
            dfs(i,j,0,"")
    print(answer)
    print("#{} {}".format(test_case,len(answer)))
