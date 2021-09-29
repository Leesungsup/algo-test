import heapq
import sys
INF=int(1e9)
n,m=map(int,input().split())
start=int(input())
distance=[INF]*(n+1)
map=[[] for _ in range(n+1)]
for i in range(n+1):
    a,b,c=map(int,sys.stdin.readline().split())
    map[a].append((b,c))
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in map[now]:
            if distance[i[0]]>dist+i[1]:
                distance[i[0]]=dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))
dijkstra(start)
print(distance)