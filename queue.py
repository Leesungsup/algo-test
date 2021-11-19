from collections import deque
def solution5(progress,speeds):
    answer=[]
    q=deque(progress)
    s=deque(speeds)
    time=0
    count=0
    while q:
        time+=1
        for i in range(progress):
            if q[0]+speeds[0]*time>=100:
                count+=1
                q.popleft()
                s.popleft()
            else:
                if count>0:
                    answer.append(count)
                    count=0
            time+=1
    return answer
def solution4(prices):
    answer=[]
    q=deque(prices)
    while q:
        x=q.popleft()
        count=0
        for i in q:
            count+=1
            if x>i:
                break
        answer.append(count)
    print(answer)
    return answer
prices=list(map(int,input().split()))
solution4(prices)
def solution3(bridge_length, weight, truck_weights):
    answer=0
    time=0
    q=deque()
    q1=deque(truck_weights)
    for i in range(bridge_length):
        q.append(0)
    print(q1[0])
    while q:
        time+=1
        q.popleft()
        if q1:
            if sum(q)+q1[0]<=weight:
                q.append(q1.popleft())
            else:
                q.append(0)
    answer=time
    print(answer)
    return answer
bridge=int(input())
weight=list(map(int,input().split()))
w=int(input())
solution3(bridge,w,weight)
def solution2(priorities,location):
    answer=0
    q=deque(priorities)
    lo=deque()
    for i in range(len(q)):
        lo.append(i)
    i=0
    while q:
        a=0
        for j in range(len(q)):
            if q[0]<q[j]:
                a=1
        if a==1:
            x=q.popleft()
            q.append(x)
            y=lo.popleft()
            lo.append(y)
        else:
            i+=1
            q.popleft()
            y=lo.popleft()
            if y==location:
                break
    print(i)
    return answer
priorities=list(map(int,input().split()))
location=int(input())
solution2(priorities,location)
def solution1(progress,speeds):
    answer=[]
    q=deque(progress)
    s=deque(speeds)
    time=0
    count=0
    while q:
        if q[0]+(s[0]*time)>=100:
            count+=1
            q.popleft()
            s.popleft()
        else:
            if count>0:
                answer.append(count)
                count=0
            time+=1
    answer.append(count)
    print(answer)
    return answer

progress=list(map(int,input().split()))
speeds=list(map(int,input().split()))
solution1(progress,speeds)
def solution5(bridge_length, weight, truck_weights):
    answer=0
    q=deque()
    truck=deque(truck_weights)
    for i in bridge_length:
        q.append(0)
    while truck:
        q.popleft()
        answer+=1
        if sum(q)+truck[0]<weight:
            q.append(truck.popleft())
        else:
            q.append(0)
    return answer
def solution6(progress,speeds):
    answer=[]
    s=deque()
    q=deque()
    for i in progress:
        q.append(i)
    for j in speeds:
        s.append(j)
    time=1
    count=0
    while q:
        if (q[0]+(s[0]*time))>=100:
            q.popleft()
            s.popleft()
            count+=1
        else:
            answer.append(count)
            count=0
        time+=1
    answer.append(count)
    return answer