import heapq
def solution(n, works):
    answer = 0
    d=[]
    q=[]
    for i in works:
        heapq.heappush(q,-i)
    #heapq.heapify(works)
    for i in range(n):
        if len(q)!=0:
            x=heapq.heappop(q)
        if x!=0:
            heapq.heappush(q,(x+1))
    for i in q:
        print(i*i)
        answer+=i*i
    #d=sorted(works,reverse=True)
    print(answer)
    return answer
solution(9,[1,1,1])
