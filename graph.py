import heapq
INF=int(1e9)
def solution(n,edge):
    answer=0
    graph=[[] for _ in range(n+1)]
    distance=[INF]*(n+1)
    visited=[0]*(n+1)
    for i in edge:
        graph[i[0]].append((i[1],1))
        graph[i[1]].append((i[0],1))
    q=[]
    distance[1]=1
    heapq.heappush(q,(0,1))
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            if distance[i[0]]<dist+i[1]:
                distance[i[0]]=dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))
    distance.remove(INF)
    m=max(distance)
    for i in distance:
        if m==i:
            answer+=1
    return answer
def solution1(n, results):
    answer = 0
    graph=[[0]*(n+1) for _ in range(n+1)]
    for i in results:
        graph[i[0]][i[1]]=1
        graph[i[1]][i[0]]=-1
    print(graph)
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k]==0:
                    continue
                if graph[i][k]==graph[k][j]:
                    graph[i][j]=graph[i][k]
                    graph[j][i]=graph[i][k]*-1
    for i in range(1,n+1):
        count=0
        for j in range(1,n+1):
            if graph[i][j]==0:
                count+=1
        if count==1:
            answer+=1
    print(graph)
    print(answer)
    return answer
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
        if distance[now]<dist:
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
    print(answer)
def solution1(n,results):
    answer=0
    win,lose={},{}
    for i in range(1,n+1):
        win[i]=set()
        lose[i]=set()
    for i in range(1,n+1):
        for r in results:
            if i==r[0]:
                win[i].add(r[1])
            if i==r[1]:
                lose[i].add(r[0])
        for j in win[i]:
            lose[j].update(lose[i])
        for j in lose[i]:
            win[j].update(win[i])
    for i in range(1,n+1):
        if len(win[i])+len(lose[i])==n-1:
            answer+=1
    return answer