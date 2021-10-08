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