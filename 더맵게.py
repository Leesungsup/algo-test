import heapq
def solution(scoville,K):
    answer=0
    heapq.heapify(scoville)
    while scoville:
        x=heapq.heappop(scoville)
        if len(scoville)==0:
            if x<K:
                answer=-1
        else:
            if x<K:
                x1=heapq.heappop(scoville)
                y=x+(x1*2)
                answer+=1
                heapq.heappush(scoville,y)
    print(answer)
scoville=list(map(int,input().split()))
K=int(input())
solution(scoville,K)