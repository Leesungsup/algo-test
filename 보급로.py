from collections import deque
import heapq
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dijkstra(d, x, y):
    queue = []
    heapq.heappush(queue, (d, x, y))
    while queue:
        d, x, y = heapq.heappop(queue)
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                # 만약 더 짧은 거리가 있다면 최소 거리로 갱신
                if distance[nx][ny] > d + graph[x][y]:
                    distance[nx][ny] = d + graph[x][y]
                    heapq.heappush(queue, (distance[nx][ny], nx, ny))
for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    distance = [[1e9]*n for _ in range(n)]
    distance[0][0] = graph[0][0]
    dijkstra(0, 0, 0)

T=int(input())
def dfs(x,y,count):
    global n
    if x==n-1 and y==n-1:
        if ro>count:
            print(ro)
            ro=count
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]>=0:
            arr[nx][ny]=-1
            dfs(nx,ny,count+arr[nx][ny])
for test_case in range(1,T+1):
    n=int(input())
    ro=987654321
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input())))
    visited=[[0]*n for _ in range(n)]
    time = [[ro]*n for _ in range(n)]
    print(arr)
    q=deque()
    visited[0][0]=1
    time[0][0]=arr[0][0]
    q.append((0,0))
    while q:
        x,y=q.popleft()
        if x==n-1 and y==n-1:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if visited[nx][ny]==0:
                    visited[nx][ny]=1
                    time[nx][ny]=time[x][y]+arr[nx][ny]
                    q.append((nx,ny))
                elif visited[nx][ny]==1:
                    if time[nx][ny]>time[x][y]+arr[nx][ny]:
                        time[nx][ny]=time[x][y]+arr[nx][ny]
    print("#{} {}".format(test_case,time[n-1][n-1]))
