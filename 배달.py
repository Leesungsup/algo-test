import heapq
INF=int(1e9)
def solution(N, road, K):
    answer = 0
    map=[[] for _ in range(N+1)]
    for i in road:
        map[i[0]].append((i[1],i[2]))
        map[i[1]].append((i[0],i[2]))
    #print(map)
    distance=[INF]*(N+1)
    q=[]
    heapq.heappush(q,(0,1))
    distance[1]=0
    while q:
        #print(q)
        dist,index=heapq.heappop(q)
        if dist>distance[index]:
            continue
        for i in map[index]:
            #print(i[1])
            if distance[i[0]]>dist+i[1]:
                distance[i[0]]=dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))
    #print(distance)
    for i in range(1,N+1):
        if distance[i]<=K:
            answer+=1
    #print(answer)
    return answer
solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)
