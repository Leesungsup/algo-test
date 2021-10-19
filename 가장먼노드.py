import heapq
INF=int(1e9)
def solution(n,edge):
    answer=0
    graph=[[] for _ in range(n+1)]
    distance=[INF]*(n+1)
    for i in edge:
        x=i[0]
        y=i[1]
        graph[x].append((y,1))
        graph[y].append((x,1))
    distance[1]=0
    q=[]
    heapq.heappush(q,(0,1))
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            if distance[i[0]]>dist+i[1]:
                distance[i[0]]=dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))
    distance.remove(INF)
    m=max(distance)
    for i in distance:
        if m==i:
            answer+=1
    return answer