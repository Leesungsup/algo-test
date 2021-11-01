import heapq
def solution(operations):
    answer=[]
    q1=[]
    q2=[]
    for i in operations:
        k=i.split()
        if k[0]=='I':
            heapq.heappush(q1,(int(k[1])))
            heapq.heappush(q2,(int(k[1])*-1))
        if k[0]=='D':
            if len(q1)==0 or len(q2)==0:
                continue
            if k[1] =='1':
                x=heapq.heappop(q2)
                q1.remove(x*-1)
            elif k[1]=="-1":
                x=heapq.heappop(q1)
                q2.remove(x*-1)
    if len(q2)!=0:
        x=heapq.heappop(q2)*-1
        answer.append(x)
    if len(q1)!=0:
        answer.append(heapq.heappop(q1))
    if len(q1)==0 or len(q2)==0:
        answer.append(0)
        answer.append(0)
    print(answer)
    return answer