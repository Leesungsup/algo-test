from collections import deque
import sys
if __name__ == "__main__":
    sys.stdin = open('data/processor.txt')
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        n = int(sys.stdin.readline())
        a = []
        pnum = 0
        ans = 1e8
        for _ in range(n):
            a.append(list(map(int, sys.stdin.readline().split())))
        print("#{} {}".format(tc, ans))
t=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(t):
    n=int(input())
    graph=[]
    visited=[[0]*n for _ in range(n)]
    print(visited)
    for i in range(n):
        graph.append(list(map(int,input().split())))
    print(graph)
    q=deque()
    q.append([(0,i) for i in range(1,n)])
    q.append([(i,0) for i in range(1,n)])
    q.append([(n-1,i) for i in range(1,n)])
    q.append([(i,n-1) for i in range(1,n)])
    while q:
        x,y=q.popleft()
        k=0
        if graph[x][y]==1:
            visited[x][y]=1
            continue
        nx=x
        ny=y
        k=0
        for i in range(n):
            if x==0:
                nx+=1
                k+=1
            elif n-1>x>0:
                ny+=1
                k+=1
            elif x==n-1:
                nx-=1
                k+=1
            elif y==n-1:
                ny-=1
                k+=1
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if visited[nx][ny]==0:
                    if graph[nx][ny]==1:
                        visited[nx][ny]=1
                        sum+=k
                        break
answer=0
n=int(input())
def dfs(check,core2,line2):
    global core
    global line
    if check==s:
        if core<core2:
            core=core2
            line=line2
        elif core2==core:
            if line>line2:
                line=line2
        return
    x=cores[check][0]
    y=cores[check][1]
    for i in range(4):
        if i==0:
            flag=0
            for i in range(x,0,-1):
                if b[i-1][y]==1:
                    flag=1
                    break
            if flag==1:
                continue
            else:
                for i in range(x,0,-1):
                    b[i-1][y]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(x,0,-1):
                    b[i-1][y]=0
                    line2-=1
        elif i==1:
            flag=0
            for i in range(y,a-1):
                if b[x][i+1]==1:
                    flag=1
                    break
            if flag==1:
                continue
            else:
                for i in range(y,a-1):
                    b[x][i+1]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(y,a-1):
                    b[x][i+1]=0
                    line2-=1
        elif i==2:
            flag=0
            for i in range(x,a-1):
                if b[i+1][y]==1:
                    flag=1
                    break
            if flag==1:
                continue
            else:
                for i in range(x,a-1):
                    b[i+1][y]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(x,a-1):
                    b[i+1][y]=0
                    line2-=1
        elif i==3:
            flag=0
            for i in range(y,0,-1):
                if b[x][i-1]==1:
                    flag=1
                    break
            if flag==1:
                continue
            else:
                for i in range(y,0,-1):
                    b[x][i-1]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(y,0,-1):
                    b[x][i-1]=0
                    line2-=1
    dfs(check+1,core2,line2)
for k in range(1,n+1):
    cores=[]
    core=0
    line=0
    a=int(input())
    b= [list(map(int, input().split())) for _ in range(a)]
    for i in range(1,a-1):
        for j in range(1,a-1):
            if b[i][j]==1:
                cores.append([i,j])
    s=len(cores)
    dfs(0,0,0)
