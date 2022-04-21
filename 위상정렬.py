from collections import deque
v,n=map(int,input().split())
ma=[[] for _ in range(v+1)]
indegree = [0] * (v + 1)
print(ma)
for i in range(n):
    a,b=map(int,input().split())
    ma[a].append(b)
    indegree[b]+=1
print(ma)
q=deque()
result=[]
for i in range(1,v+1):
    if indegree[i]==0:
        q.append(i)
while q:
    start=q.popleft()
    result.append(start)
    for i in ma[start]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)
for i in range(len(result)):
    print(result[i])