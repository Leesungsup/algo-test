graph=[]
#n,m=int(input().split())
for i in range(19):
    graph.append(list(map(int,input().split())))
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    for j in range(19):
        if graph[x-1][j]==1:
            graph[x-1][j]=0
        else:
            graph[x-1][j]=1
        if graph[j][y-1]==1:
            graph[j][y-1]=0
        else:
            graph[j][y-1]=1
for i in range(19):
    print(graph[i])
