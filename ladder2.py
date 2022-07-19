import sys
sys.stdin = open("input.txt", "r")
def dfs(x,y,i,count):
    if x==99:
        if i==100:
            m[0]=count
        elif m[i]==0:
            m[i]=count
        return
    if y-1>=0 and y-1<100 and arr[x][y-1]!=0 and (arr[x][y-1]==1 or arr[x][y-1]!=i):
        ny=y-1
        nx=x
    elif y+1>=0 and y+1<100 and arr[x][y+1]!=0 and (arr[x][y+1]==1 or arr[x][y+1]!=i):
        ny=y+1
        nx=x
    elif 0<=x+1<100:
        nx=x+1
        ny=y
    if arr[nx][ny]!=0 and (arr[nx][ny]==1 or arr[nx][ny]!=i):
        arr[nx][ny]=i
        dfs(nx,ny,i,count+1)
for test_case in range(1,11):
    T=int(input())
    arr=[]
    m=[0]*100
    for i in range(100):
        arr.append(list(map(int,input().split())))
    s=[]
    for i in range(100):
        if arr[0][0]==1:
            arr[0][0]=100
            dfs(0,i,100,0)
        elif arr[0][i]==1:
            arr[0][i]=i
            dfs(0,i,i,0)
    print(m)
    m1=987654321
    m2=0
    for i in range(100):
        if m1>=m[i] and m2<i:
            m1=m[i]
            m2=i
    print("#{} {}".format(T,m2))
