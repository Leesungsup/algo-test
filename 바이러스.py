from collections import deque
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result.append(i)
            dfs(graph, i, visited)

n = int(input())
network = int(input())
graph = [[] for _ in range(n+1)]
result = []
visited = [False] * (n+1)

for i in range(network):
    node, node2 = map(int, input().split())
    graph[node].append(node2)
    graph[node2].append(node)

dfs(graph, 1, visited)
print(len(result))

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)
q=deque()
q.append(1)
while q:
    x=q.popleft()
    visited[x]=1
    for i in graph[x]:
        if visited[i]==0:
            q.append(i)
print(visited)

def dfs(graph, v, visited):
    for i in graph[v]:
        if i not in visited:
            visited.append(i)
            dfs(graph, i, visited)

n = int(input())
network = int(input())
graph = [[] for _ in range(n+1)]
visited = []

for i in range(network): # 그래프는 양방향이니까 거꾸로도 추가시켜야한다.
    node, node2 = map(int, input().split())
    graph[node].append(node2)
    graph[node2].append(node)

dfs(graph, 1, visited)
print(len(visited)-1)