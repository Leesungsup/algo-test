from collections import deque
n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
def bfs(x):
    q=deque()
    q.append(x)
    while q:
        x=q.popleft()
        for i in graph[x]:
            if distance[i]==0:
                q.append(i)
                distance[i]=distance[x]+1

bfs(x)