import heapq
import collections
import sys
T=int(input())
def prim(start):
    global total_weight
    #q.append(graph[start])
    #heapq.heapify(q)
    visited[start]=1
    q=[]
    heapq.heappush(q,graph[start])
    mst=[]
    while q:
        weight,u,v=heapq.heappop(q)
        if visited[v]==0:
            visited[v]=1
            mst.append((u,v))
            total_weight+=weight
            for j in graph[v]:
                if visited[j[2]]==0:
                    heapq.heappush(q,j)
for test_case in range(1,T+1):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    visited=[0]*(v+1)
    total_weight=0
    for i in range(e):
        u,v,weight=map(int,input().split())
        graph[u].append((v,weight))
    q=[]
    heapq.heapify(q)
    prim(1)
    print("#{} {}".format(test_case,total_weight))
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())
graph = collections.defaultdict(list)
visited = [0] * (n+1)

# 무방향 그래프 생성
for i in range(m): # 간성 정보 입력 받기
    u, v, weight = map(int,input().split())
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])


# 프림 알고리즘
def prim(graph, start_node):
    visited[start_node] = 1 # 방문 갱신
    candidate = graph[start_node] # 인접 간선 추출
    heapq.heapify(candidate) # 우선순위 큐 생성
    mst = [] # mst
    total_weight = 0 # 전체 가중치

    while candidate:
        weight, u, v = heapq.heappop(candidate) # 가중치가 가장 적은 간선 추출
        if visited[v] == 0: # 방문하지 않았다면
            visited[v] = 1 # 방문 갱신
            mst.append((u,v)) # mst 삽입
            total_weight += weight # 전체 가중치 갱신

            for edge in graph[v]: # 다음 인접 간선 탐색
                if visited[edge[2]] == 0: # 방문한 노드가 아니라면, (순환 방지)
                    heapq.heappush(candidate, edge) # 우선순위 큐에 edge 삽입

    return total_weight

print(prim(graph,1))