from collections import deque
def print_out(h,n,m):
    c = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k]==0:
                    return False
                if c < board[i][j][k]:
                    c = board[i][j][k]
    return c-1
m,n,h=map(int,input().split())
board=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
# print(board)
q=deque()
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
di=False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k]==1:
                q.append((i,j,k))
            elif board[i][j][k]==0:
                di=True
#             print(board[i][j][k],end="")
#         print()
#     print()
# print(q)
if di:
    while q:
        z,x,y=q.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0<=nz<h and 0<=ny<m and 0<=nx<n and board[nz][nx][ny]==0:
                board[nz][nx][ny]=board[z][x][y]+1
                q.append((nz,nx,ny))
    c=print_out(h,n,m)
    if c:
        print(c)
    else:
        print(0)
else:
    print(0)