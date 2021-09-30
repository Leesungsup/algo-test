from collections import deque
def solution(array,location):
    answer=0
    q=[]
    q1=[]
    index=[]
    q=deque()
    q1=deque()
    index=deque()
    for i in range(len(array)):
        q.append(array[i])
        q1.append(i)
    a=0
    while q:
        i=0
        for j in range(len(q)):
            if q[i]<q[j]:
                a=1
        if a==0:
            q.popleft()
            y1=q1.popleft()
            index.append(y1)
        else:
            x=q.popleft()
            q.append(x)
            x1=q1.popleft()
            q1.append(x1)
            a=0
    index1=0
    for i in index:
        index1+=1
        if i==location:
            answer=index1
    print(answer)


array=list(map(int,input().split()))
location=int(input())
solution(array,location)