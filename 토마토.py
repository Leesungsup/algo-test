from collections import deque
m,n,h=map(int,input().split())
#board=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]
q = deque()
def print_max():
    m = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if not board[i][j][k]:
                    return False
                if m < board[i][j][k]:
                    m = board[i][j][k]
    return m-1
def bfs():
    while q:
        z,y,x=q.popleft()
        for i in range(6):
            nz=z+dz[i]
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and board[nz][ny][nx]==0:
                board[nz][ny][nx]+=1
                q.append((nz,ny,nx))
di=False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                q.append((i, j, k))
            else:
                di=True
if not di:
    print(0)
else:
    bfs()
    out = print_max()
    if not out:
        print(-1)
    else:
        print(out)
