graph=[]
for i in range(10):
    graph.append(list(map(int,input().split())))
print(graph)
x=1
y=1
graph[1][1]=9
while True:
    if graph[x][y]==2:
        graph[x][y]=9
        break
    graph[x][y]=9
    if graph[x][y+1]!=1:
        y=y+1
    elif graph[x][y+1]==1 and graph[x+1][y]!=1:
        x=x+1
    else:
        break
for i in range(10):
    print(graph[i])
