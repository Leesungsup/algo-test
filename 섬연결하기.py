import heapq
def prim(graph,start_node,visited):
    total=0
    visited[start_node]=1
    candidate=graph[start_node]
    heapq.heapify(candidate)
    mst=[]
    while candidate:
        weight,u,v=heapq.heappop(candidate)
        if visited[v]==0:
            visited[v]=1
            mst.append((u,v))
            total+=weight
            for i in graph[v]:
                if visited[i[2]]==0:
                    heapq.heappush(candidate,i)
    return total
def solution(n,costs):
    answer=0
    graph=[[] for _ in range(n+1)]
    visited=[0]*(n+1)
    for i in costs:
        graph[i[0]].append(i[2],i[0],i[1])
        graph[i[1]].append(i[2],i[1],i[0])
    answer=prim(n,graph,visited)
    return answer
def prim1(graph,start_node,visited):
    total=0
    mst=[]
    visited[start_node]=0
    candidate=graph[start_node]
    while candidate:
        weight,u,v=heapq.heappop(candidate)
        if visited[v]==0:
            visited[v]=1
            mst.append((u,v))
            total+=weight
            for i in graph[v]:
                if visited[i[2]]==0:
                    heapq.heappush(candidate,i)
    return total
def solution1(n,costs):
    answer=0
    graph=[[] for _ in range(n+1)]
    visited=[0]*(n+1)
    for i in costs:
        graph[i[0]].append((i[2],i[0],i[1]))
        graph[i[1]].append((i[2],i[1],i[0]))
    answer=prim1(graph,0,visited)
    return answer