import heapq
def solution1(board):
    answer=0
    q=[]
    heapq.heappush(q,(0,0,0))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    n=len(board)
    board[0][0]=1
    cx1=0
    cy1=0
    cx2=0
    cy2=0
    k=-1
    c=0
    while q:
        k+=1
        d,x,y=heapq.heappop(q)
        print(d)
        print(x,y)
        if k<2:
            cx2=cx1
            cy2=cy1
            cx1=x
            cy1=y
        else:
            print(cx2,cx1,x)
            print(cy2,cy1,y)
            if (cx2==cx1 and cx1!=x) or ((cy2==cy1) and (cy1!=y)):
                c+=1
        if x==n-1 and y==n-1:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if board[nx][ny]==0:
                    board[nx][ny]=1
                    heapq.heappush(q,(d+1,nx,ny))
    print(c)
    print(d)
    return answer
import sys
import collections
def solution(board):
    INF=sys.maxsize
    n=len(board)
    answer = INF
    dd=[0, 1, 2, 3]
    dy=[0, 1, 0, -1]
    dx=[1, 0, -1, 0]
    dist=[[[INF for _ in range(len(board[0]))] for _ in range(len(board))] for _ in range(4)]
    q=collections.deque()
    q.append([0, 0, 0, 0])
    q.append([0, 0, 0, 1])
    while q:
        y, x, cost, d=q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<n and board[ny][nx]==0:
                n_cost=cost+1
                if d!=dd[i]:
                    n_cost+=5
                if dist[dd[i]][ny][nx]>n_cost:
                    dist[dd[i]][ny][nx]=n_cost
                    if ny==n-1 and nx==n-1:
                        continue
                    q.append([ny, nx, n_cost, dd[i]])
    for i in range(4):
        answer=min(answer, dist[i][n-1][n-1])
    answer*=100
    return answer
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
