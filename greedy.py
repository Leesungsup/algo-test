import heapq
def prim(graph,start_node,visited):
    visited[start_node]=1
    total=0
    mst=[]
    candidate=graph[start_node]
    heapq.heapify(candidate)
    while candidate:
        dist,u,v=heapq.heappop(candidate)
        if visited[v]==0:
            total+=dist
            visited[v]=1
            mst.append((u,v))
            for i in graph[v]:
                if visited[i[2]]==0:
                    heapq.heappush(candidate,i)
    return total
def solution3(n,costs):
    answer=0
    graph=[[] for _ in range(n+1)]
    for i in costs:
        graph[i[0]].append((i[2],i[0]))
        graph[i[1]].append((i[2],i[0]))
    visited=[0]*(n+1)
    answer=prim(graph,0,visited)
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