import sys
INF=int(1e9)
n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if i==j:
            graph[i][j]=0
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a][b]=c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
print(graph)
