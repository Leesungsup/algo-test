graph=[]
n,m=map(int,input().split())
for i in range(n):
    graph.add(list(map(int,input().split())))

print(graph)

for i in range(1,n+1):
    for j in range(1,m+1):
        graph[i][j]+=max(graph[i-1][j],graph[i][j-1])
print(graph[n][m])