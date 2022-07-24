import math
import heapq
T=int(input())
def prim(start_node):
    mst=[]
    total_weight=0
    visited[start_node]=1
    q=graph[start_node]
    heapq.heapify(q)
    while q:
        weight,u,v=heapq.heappop(q)
        if visited[v]==0:
            visited[v]=1
            mst.append((u,v))
            total_weight+=weight
            for edge in graph[v]:
                if visited[edge[2]] == 0:
                    heapq.heappush(q, edge)
    return total_weight
for test_case in range(1,T+1):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    e=float(input())
    graph=[[] for _ in range(n+1)]
    visited=[0]*(n+1)
    for i in range(n):
        x1=x[i]
        y1=y[i]
        for j in range(n):
            graph[i+1].append([((x1-x[j])**2+(y1-y[j])**2)*e,(i+1),(j+1)])
            graph[j+1].append([((x1-x[j])**2+(y1-y[j])**2)*e,(j+1),(i+1)])
    an=prim(1)
    print("#{} {}".format(test_case,an))
