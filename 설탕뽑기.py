w,h=map(int,input().split())
n=int(input())
graph=[[0]*(w) for _ in range(h)]
print(graph)
for i in range(n):
    l,d,x,y=map(int,input().split())
    for j in range(l):
        if d==0:
            graph[x-1][y-1+j]=1
        else:
            graph[x-1+j][y-1]=1
print(graph)
