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
def dfs(i,n,visited,computers):
    visited[i]=1
    for connect in range(n):
        if i!=connect and computers[i][connect]==1:
            dfs(connect,n,visited,computers)
def solution2(n,computers):
    answer=0
    visited=[0]*(n)
    for i in range(n):
        if visited[i]==0:
            dfs(i,n,visited,computers)
    return answer
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    graph.append(list(map(int,input().split())))
def dfs(x,y):
    if x>=n or x<0 or y>=m or y<0:
        return False
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                dfs(nx,ny)
                return True
    return False
answer=0
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            answer+=1
n,m=map(int,input().split())
for i in range(n):
    graph.append(list(map(int,input().split())))
def bfs(x,y):
    q=deque((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if graph[nx][ny]==1:
                    graph[nx][ny]=graph[x][y]+1
                    q.append((nx,ny))
bfs(0,0)
def dfs(begin,target,words,visited):
    num=0
    stack=[begin]
    while stack:
        s=stack.pop()
        if s==target:
            return num
        for w in range(len(words)):
            if len([i for i in range(len(s)) if words[w][i]!=s[i]])==1:
                if visited[w]==1:
                    continue
                visited[w]=1
                stack.append(words[w])
        num+=1
def solution3(begin,target,words):
    answer=0
    visited=[[] for _ in range(0,len(words))]
    if target not in words:
        return answer
    else:
        dfs(begin,target,words,visited)
    return answer
def dfs(begin,target,words,visited):
    num=0
    stack=[begin]
    while stack:
        s=stack.pop()
        if s==target:
            return num
        for w in range(len(words)):
            if len([i for i in range(len[s[i]]) if s[i]!=words[w][i]])==1:
                if visited[w]==1:
                    continue
                visited[w]=1
                stack.append(words[w])
        num+=1
def solution3(begin,target,words):
    answer=0
    visited=[[] for _ in range(0,len(words))]
    if target not in words:
        return answer
    else:
        answer=dfs(begin,target,words,visited)
    return answer
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
from collections import defaultdict
def solution4(tickets):
    answer=[]
    d=defaultdict(list)
    for i in tickets:
        d[i[0]].append(i[1])
    for i in d.keys():
        d[i[0]].sort(reverse=True)
    stack=['ICN']
    while stack:
        tmp=stack[-1]
        if not d[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(d[tmp].pop())
    answer.reverse()
    return answer
from collections import deque
def solution4(tickets):
    answer=[]
    d=defaultdict(list)
    for i in tickets:
        d[i[0]].append(i[1])
    for i in d.keys():
        d[i].sort(reverse=True)
    stack=['ICN']
    while stack:
        s=stack.pop()
        if not d[s]:
            answer.append(stack.pop())
        else:
            stack.append(d[s].pop())
    answer.reverse()
    return answer
from collections import deque
def solution5(numbers,target):
    answer=0
    q=deque()
    q.append((-numbers[0],0))
    q.append((numbers[0],0))
    n=len(numbers)
    while q:
        num,i=q.popleft()
        if i-1==n:
            if num==target:
                answer+=1
        else:
            q.append((num+numbers[i+1],i+1))
            q.append((num-numbers[i+1],i+1))
    return answer
def solution6(n,computers):
    answer=0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if computers[i][j]==0:
                    if computers[i][k]!=0 and computers[k][j]!=0:
                        computers[i][j]=computers[i][k]+computers[k][j]
    max=-987654321
    for i in computers:
        num=0
        for j in i:
            if j==0:
                num+=1
        if max<num:
            max=num
    answer=max
    return answer
def dfs(begin,target,words,visited):
    num=0
    stack=[begin]
    while stack:
        s=stack.pop()
        if s==target:
            return num
        for w in range(len(words)):
            if len([i for i in range(len[s[i]]) if s[i]!=words[w][i]])==1:
                if visited[w]==1:
                    continue
                visited[w]=1
                stack.append(words[w])
        num+=1
def solution3(begin,target,words):
    answer=0
    visited=[[] for _ in range(0,len(words))]
    if target not in words:
        return answer
    else:
        answer=dfs(begin,target,words,visited)
    return answer
def dfs1(begin,target,words,visited):
    num=0
    q=[begin]
    while q:
        s=q.pop()
        if s==target:
            return num
        for w in range(len(words)):
            if len([i for i in range(len(s)) if s[i]!=words[w][i]])==1:
                if visited[w]==1:
                    continue
                visited[w]=1
                q.append(words[w])
        num+=1

def solution7(begin,target,words):
    answer=0
    visited=[[] for i in range(0,len(words))]
    if target not in words:
        return answer
    else:
        dfs1(begin,target,words,visited)
def solution(tickets):
    answer = []
    return answer