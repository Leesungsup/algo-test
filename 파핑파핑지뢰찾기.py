T=int(input())
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
def dfs(x,y):
    global time,n
    print("----------------")
    for i in range(n):
        print(visited[i])
    k=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n and map[nx][ny]=='*':
            k=1
    if k==0:
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny]==0:
                visited[nx][ny]=1
                dfs(nx,ny)
    return
for test_case in range(1,T+1):
    n=int(input())
    map=[[] for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        map[i]=list(input())
    print(map)
    print(visited)
    time=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and map[i][j]=='.':
                k=0
                for c in range(8):
                    nx=i+dx[c]
                    ny=j+dy[c]
                    if nx>=0 and nx<n and ny>=0 and ny<n and map[nx][ny]=='*':
                        k=1
                        visited[nx][ny]=2
                        print(i,j,nx,ny)
                        break
                if k==0:
                    print("agah")
                    print(i,j)
                    time+=1
                    visited[i][j]=1
                    for c in range(8):
                        nx=i+dx[c]
                        ny=j+dy[c]
                        if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny]==0:
                            visited[nx][ny]=1
                            dfs(nx,ny)
            elif map[i][j]=='*':
                visited[i][j]=2
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                time+=1
    print("#{} {}".format(test_case,time))

from collections import deque

def bfs(index):
    queue = deque()
    queue.append(index)

    while queue:
        r, c = queue.popleft()
        for i in range(8):
            dr, dc = r + dx[i], c + dy[i]
            if 0 <= dr < N and 0 <= dc < N and V[dr][dc] == False:
                V[dr][dc] = True
                if M[dr][dc] == 0:
                    queue.append((dr, dc))


def get_mine(index):
    r, c = index
    mine = 0
    for i in range(8):
        dr, dc = r + dx[i], c + dy[i]
        if 0 <= dr < N and 0 <= dc < N and M[dr][dc] == '*':
            mine += 1
    return mine


for T in range(1, int(input())+1):
    N = int(input())
    M = [list(input()) for _ in range(N)]
    safe_zone = []
    ans = 0

    for i in range(N):
        for j in range(N):
            if M[i][j] == '.':
                M[i][j] = get_mine((i, j))
            if M[i][j] == 0:
                safe_zone.append((i, j))

    V = [[False for _ in range(N)] for _ in range(N)]

    for i in safe_zone:
        r, c = i
        if V[r][c]:
            continue
        V[r][c] = True
        bfs(i)
        ans += 1

    for i in range(N):
        for j in range(N):
            if V[i][j] == False and M[i][j] != '*':
                ans += 1

    print('#{} {}'.format(T, ans))
