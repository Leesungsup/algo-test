from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q=deque()
    for i in range(cacheSize):
        q.append('')
    #print(q)
    for i in cities:
        if len(q)!=0:
            if i.lower() in q:
                answer+=1
                q.remove(i.lower())
                q.append(i.lower())
            else:
                answer+=5
                q.popleft()
                q.append(i.lower())
        else:
            answer+=5
    #print(answer)
    return answer