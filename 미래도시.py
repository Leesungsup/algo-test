from collections import deque
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[-1]*(n+1)
distance1=[-1]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
x,k=map(int,input().split())
result=0
result1=0
def bfs(v):
    global result
    q=[]
    q=deque()
    q.append(v)
    distance[v]=0
    while q:
        v=q.popleft()
        if v==k:
            result=distance[k]
            break
        for i in graph[v]:
            if distance[i]==-1:
                distance[i]=distance[v]+1
                q.append(i)
def bfs1(v):
    global result1
    q1=[]
    q1=deque()
    q1.append(v)
    distance1[v]=0
    while q1:
        v=q1.popleft()
        if v==x:
            result1=distance1[k]
            break
        for i in graph[v]:
            if distance1[i]==-1:
                distance1[i]=distance1[v]+1
                q1.append(i)
bfs(1)
bfs(k)
if result==-1 or result1==-1:
    print(-1)
else:
    print(result+result1)