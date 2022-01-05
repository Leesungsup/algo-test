import heapq
from itertools import combinations
INF=int(1e9)
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(n):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
distance=[INF]*(n+1)
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            if distance[i[0]]>dist+i[1]:
                distance[i[0]]=dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))
def prim(graph,start_node,visited):
    visited[start_node]=1
    total_weight=0
    mst=[]
    candidate=graph[start_node]
    heapq.heapify(candidate)
    while candidate:
        weight,u,v=heapq.heappop(candidate)
        if visited[v]==0:
            total_weight+=weight
            visited[v]=1
            mst.append((u,v))
            for i in graph[v]:
                if visited[i[2]]==0:
                    heapq.heappush(candidate,i)
    return total_weight
def solution(n,costs):
    answer=0
    graph=[[] for _ in range(n+1)]
    for i in costs:
        graph[i[0]].append((i[2],i[0],i[1]))
        graph[i[1]].append((i[2],i[1],i[0]))
    visited=[0]*n
    prim(graph,0,visited)
def solution(people,limit):
    answer=0
    people.sort()
    while people:
        if len(people)==1:
            answer+=1
            break
        if people[0]+people[-1]<=limit:
            del people[0]
            del people[-1]
        else:
            del people[-1]
        answer+=1
    return answer
def solution(number,k):
    answer=[]
    numbers=list(number)
    stack=[]
    for i in numbers:
        if not stack:
            stack.append(i)
            continue
        if k>0:
            while stack[-1]<i:
                stack.pop()
                k-=1
                if k<=0 and not stack:
                    break
        stack.append(i)
    answer=stack[:-k] if k>0 else stack
    return ''.join(answer)
def solution(number, k):
    answer = ''
    s=list(number)
    max=-987654321
    for j in combinations(s,len(s)-k):
        num=''.join(j)
        if max<int(num):
            max=int(num)
            d=num
    answer=d
    print(answer)
    return answer
def solution(name):
    answer=0
    n=len(name)
    for i,k in enumerate(name):
        answer+=min(ord(k)-ord('A'),ord('Z')-ord(k)+1)
        next=i+1
        while next<len(name) and name[next]=='A':
            next+=1
        n=min(n,i+i+len(name)-next)
    answer+=n
def solution(n, lost, reserve):
    answer = 0
    lost_set=set(lost)-set(reserve)
    reverve_set=set(reserve)-set(lost)
    for i in reverve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    answer=n-len(lost_set)
    return answer
def prim(graph,start_node,visited):
    visited[start_node]=1
    q=graph[start_node]
    heapq.heapify(q)
    mst=[]
    total=0
    while q:
        weight,u,v=heapq.heappop(q)
        if visited[v]==0:
            visited[v]=1
            mst.append((u,v))
            total+=weight
            for i in graph[v]:
                if visited[i[2]]==0:
                    heapq.heappush(q,i)
    return total
def solution4(n,costs):
    answer=0
    visited=[0]*(n+1)
    graph=[[] for _ in range(n+1)]
    for i in costs:
        graph[i[0]].append((i[2],i[0],i[1]))
        graph[i[1]].append((i[2],i[1],i[0]))
    prim(graph,0,visited)
    return answer
def solution2(people,limit):
    answer=0
    people.sort()
    while people:
        if len(people)==1:
            answer+=1
            break
        if people[0]+people[-1]<=limit:
            del people[0]
            del people[-1]
        else:
            del people[-1]
        answer+=1
    return answer
def solution1(name):
    answer=0
    n=len(name)
    for i,k in enumerate(name):
        answer+=min(ord(k)-ord('A'),ord('Z')+ord(k)+1)
        next=i+1
        while next<len(name) and name[next]=='A':
            next+=1
        n=min(n,i+i+len(name)-next)
    answer+=n
    return answer
def solution(n,lost,reserve):
    answer=0
    lost_set=set(lost)-set(reserve)
    reserve_set=set(reserve)-set(lost)
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    answer=n-len(lost_set)
    return answer