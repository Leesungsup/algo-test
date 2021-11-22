import heapq
INF=int(1e9)
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
