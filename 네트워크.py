from collections import deque
def solution(n,computers):
    answer=0
    q=deque()
    visited=[0]*n
    while 0 in visited:
        q.append(visited.index(0))
        while q:
            v=q.popleft()
            visited[v]=1
            for i in range(n):
                if visited[v]==0 and computers[v][i]==1:
                    q.append(i)
        answer+=1
    return answer
def solution(n,computers):
    answer=0
    q=[]
    q=deque()
    visited=[0]*(n)
    while 0 in visited:
        q.append(visited.index(0))
        while q:
            v=q.popleft()
            visited[v]=1
            for i in range(n):
                if visited[i]==0 and computers[v][i]==1:
                    q.append(i)
        answer+=1
    print(answer)