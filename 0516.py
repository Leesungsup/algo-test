from collections import defaultdict

def dfs(graph, node, visited):
    visited[node] = True
    max_distance = 0

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            distance = dfs(graph, neighbor, visited) + weight
            if distance > max_distance:
                max_distance = distance

    return max_distance

def find_diameter(graph):
    n = len(graph)
    diameter = 0

    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        distance = dfs(graph, i, visited)
        if distance > diameter:
            diameter = distance

    return diameter

n = int(input())  # 건물 수
graph = defaultdict(list)

for _ in range(n - 1):
    a, b, weight = map(int, input().split())  # 건물 간 연결 및 가중치
    graph[a].append((b, weight))
    graph[b].append((a, weight))

result = find_diameter(graph)
print(result)

n=int(input())
graph=[[] for _ in range(n+1)]
max=0
for i in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
def dfs(graph,v,visited,depth):
    global max
    if depth>max:
        max=depth
    for i,j in graph[v]:
        if i not in visited:
            visited.append(i)
            depth+=j
            dfs(graph,i,visited,depth)
for i in range(1,n+1):
    visited=[]
    dfs(graph,i,visited,0)
print(max)

n,k=map(int,input().split())
graph=[[] for _ in range(n)]
visited=[]
for i in range(k):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,v,visited):
    for i in graph[v]:
        if i not in visited:
            visited.append(i)
            dfs(graph, i, visited)

dfs(graph,0,visited)
print(visited)
if len(visited)==n:
    print(1)
else:
    print(0)

