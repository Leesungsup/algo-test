from collections import deque
def solution(numbers,target):
    answer=0
    q=[]
    n=len(numbers)
    q=deque()
    q.append((-numbers[0],0))
    q.append((numbers[0],0))
    while q:
        num,i=q.popleft()
        if i+1==n:
            if target==num:
                answer+=1
        else:
            q.append((num-numbers[i+1],i+1))
            q.append((num+numbers[i+1],i+1))
    print(answer)
numbers=list(map(int,input().split()))
target=int(input())
solution(numbers,target)
def solution1(numbers,target):
    answer=0
    q=[]
    n=len(numbers)
    q=deque()
    q.append((numbers[0],0))
    q.append((-numbers[0],0))
    while q:
        num,i=q.popleft()
        if i+1==n:
            if num==target:
                answer+=1
        else:
            q.append((num+numbers[i+1],i+1))
            q.append((num-numbers[i+1],i+1))
    print(answer)
    return answer
def dfs(i,n,visited,computers):
    visited[i]=1
    for connect in range(n):
        if i!= connect and computers[i][connect]==1:
            if visited[connect]==0:
                dfs(connect,n,visited,computers)
def solution2(n,computers):
    answer=0
    visited=[0]*(n)
    for i in range(n):
        if visited[i]==0:
            dfs(i,n,visited,computers)
            answer+=1
    return answer
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    graph.append(list(map(int,input().split())))
def dfs(x,y):
    q=deque((x,y))
    while q:
        x,y=q.popleft()