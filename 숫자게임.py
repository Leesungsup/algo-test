import heapq
def solution(A,B):
    answer=0
    A=[-i for i in A]
    B=[-i for i in B]
    heapq.heapify(A)
    heapq.heapify(B)
    for i in range(len(A)):
        a=heapq.heappop(A)
        b=heapq.heappop(B)
        if -a<-b:
            answer+=1
        else:
            heapq.heappush(B,b)
    return answer