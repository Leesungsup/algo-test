from collections import deque
def solution(prices):
    answer=[]
    q=deque(prices)
    while q:
        count=0
        x=q.popleft()
        for j in q:
            count+=1
            if x>j:
                break
        answer.append(count)
    print(answer)

price=list(map(int,input().split()))
solution(price)