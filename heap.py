import heapq
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
