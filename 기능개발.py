from collections import deque
def solution(progress,speeds):
    answer=[]
    q=[]
    s=[]
    q=deque()
    s=deque()
    for i in progress:
        q.append(i)
    for i in speeds:
        s.append(i)
    time=0
    count=0
    while q:
        if (q[0]+(s[0]*time))>=100:
            s.popleft()
            q.popleft()
            count+=1
        else:
            if count>0:
                answer.append(count)
                count=0
            time+=1
    answer.append(count)
    print(answer)
array=list(map(int,input().split()))
array1=list(map(int,input().split()))
solution(array,array1)
from collections import deque
def solution1(progress,speeds):
    answer=[]
    q=[]
    s=[]
    q=deque()
    s=deque()
    for i in progress:
        q.append(i)
    for i in speeds:
        s.append(i)
    time=0
    count=0
    while q:
        if (q[0]+(s[0]*time))>=100:
            s.popleft()
            q.popleft()
            count+=1
        else:
            if count>0:
                answer.append(count)
                count=0
            time+=1
    answer.append(count)
    print(answer)
array=list(map(int,input().split()))
array1=list(map(int,input().split()))
solution1(array,array1)