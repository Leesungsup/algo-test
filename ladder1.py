import sys
sys.stdin = open("input.txt", "r")
def dfs(x,y):
    if x==0:
        return
    if y-1>=0 and y-1<100 and arr[x][y-1]==1:
        ny=y-1
        nx=x
    elif y+1>=0 and y+1<100 and arr[x][y+1]==1:
        ny=y+1
        nx=x
    elif 0<=x-1<100:
        nx=x-1
        ny=y
    if arr[nx][ny]==1:
        arr[nx][ny]=3
        dfs(nx,ny)
for test_case in range(1,11):
    T=int(input())
    arr=[]
    for i in range(100):
        arr.append(list(map(int,input().split())))
    s=[]
    for i in range(100):
        if arr[99][i]==2:
            s.append(i)
            arr[99][i]=3
            dfs(99,i)
            break
    for i in range(100):
        if arr[0][i]==3:
            #print(i)
            start=i
            break
    print("#{} {}".format(T,start))
