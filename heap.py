import heapq
INF=int(1e9)
def solution6(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1

    return answer // len(jobs)
def solution5(operations):
    answer = []
    q=[]
    q1=[]
    for i in operations:
        s=i.split()
        print(s)
        if s[0]=='I':
            heapq.heappush(q,int(s[1]))
            heapq.heappush(q1,int(s[1])*-1)
        else:
            if len(q1)==0 or len(q)==0:
                continue
            elif s[1]=='1':
                x=heapq.heappop(q1)
                q.remove(x*-1)
            else:
                x=heapq.heappop(q)
                q1.remove(x*-1)
        print(q)
    if len(q)==0 or len(q1==0):
        answer=[0,0]
    else:
        x=heapq.heappop(q)
        answer.append(x)
        x=heapq.heappop(q1)
        answer.append(x*-1)
    return answer
def solution4(scoville,K):
    answer=0
    heapq.heapify(scoville)
    time=0
    while scoville:
        x=heapq.heappop(scoville)
        if len(scoville)==0:
            if x<K:
                answer=-1
                return answer
        else:
            if x<K:
                x1=heapq.heappop()
                x2=x+(x1*2)
                heapq.heappush(scoville,x2)
                answer+=1
            else:
                break
    return answer
def prim(graph,start,visited):
    mst=[]
    q=[]
    visited[start]=1
    heapq.heappush(q,(graph[start]))
    while q:
        d,n,v=heapq.heappop(q)
        if visited[v]==1:
            continue
        else:
            visited[v]=1
            mst.append((n,v))
            for i in graph[v]:
                if visited[i[2]]==0:
                    heapq.heappush(q,(i))
def solution3(n,costs):
    visited=[0]*(n+1)
    graph=[[] for _ in range(n+1)]
    for i in costs:
        graph[i[0]].append((i[2],i[0],i[1]))
        graph[i[1]].append((i[2],i[1],i[0]))
    prim(graph,0,visited)
def solution2():
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    dist=[INF]*(n+1)
    for i in range(n):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
    q=[]
    dist[0]=0
    heapq.heappush(q,(0,0))
    while q:
        d,now=heapq.heappop(q)
        if dist[now]<d:
            continue
        for i in graph[now]:
            if dist[i[0]]>d+i[1]:
                dist[i[0]]=d+i[1]
                heapq.heappush(q,(d+i[1],i[0]))
def solution1(jobs):
    answer=0
    now=0
    q=[]
    i=0
    time=-1
    while i<len(jobs):
        for job in jobs:
            if time<job[0]<=now:
                heapq.heappush(q,(job[1],job[0]))
        if len(q)>0:
            dist,now=heapq.heappop(q)
            time=now
            now+=dist
            answer+=(now-time)
            i+=1
        else:
            now+=1
def solution(scoville,k):
    answer=0
    heapq.heapify(scoville)
    while scoville:
        x=heapq.heappop(scoville)
        if len(scoville)==0:
            if x<k:
                answer=-1
        else:
            if x<k:
                x1=heapq.heappop(scoville)
                y=x+(x1*2)
                answer+=1
                heapq.heappush(scoville,y)
    print(answer)
scoville=list(map(int,input().split()))
k=int(input())
solution(scoville,k)
