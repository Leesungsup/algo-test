import copy
from collections import deque
import sys
graph=[]
n,m=map(int,input().split())
t=[]
water=[]
for i in range(n):
    k=list(input())
    for j in range(m):
        if k[j]=='L':
            t.append((i,j))
        elif k[j]=='.':
            water.append((i,j))
    graph.append(k)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=1
o=False
while True:
    graph1=copy.deepcopy(graph)
    q=deque(t)
    q1=deque(water)
    while q:
        x,y=q.popleft()
        graph1[x][y]='.'
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph1[nx][ny]=='.' or graph1[nx][ny]=='L':
                    if graph1[nx][ny]=='L':
                        o=True
                        break
                    q.append((nx,ny))
    if o:
        break
    while q1:
        x,y= q1.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            print(nx,ny)
            if 0<=nx<n and 0<=ny<m:
                if graph1[nx][ny]=='X':
                    graph1[nx][ny]='.'
                    water.append((nx,ny))
    count+=1

print(count)

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not c[nx][ny]:
                    if a[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1
    return 0

def melt():
    while wq:
        x, y = wq.popleft()
        if a[x][y] == 'X':
            a[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not wc[nx][ny]:
                    if a[nx][ny] == 'X':
                        wq_temp.append([nx, ny])
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1

m, n = map(int, input().split())
c = [[0]*n for _ in range(m)]
wc = [[0]*n for _ in range(m)]

a, swan = [], []
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if a[i][j] == 'L':
            swan.extend([i, j])
            wq.append([i, j])
        elif a[i][j] == '.':
            wc[i][j] = 1
            wq.append([i, j])

x1, y1, x2, y2 = swan
q.append([x1, y1])
a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', 1
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1