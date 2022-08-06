from collections import deque
for test_case in range(1,11):
    n,start=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    arr=list(map(int,input().split()))
    print(arr)
    for i in range(0,n,2):
        graph[arr[i]].append(arr[i+1])
    print(graph)
    q=deque()
    visited=[0]*(n+1)
    q.append((0,start))
    while q:
        dist,v=q.popleft()
        for i in graph[v]:
            if visited[i]==0:
                visited[v]=dist+1
                q.append((dist+1,i))
    print(visited)
    m=max(visited)
    answer=-987654321
    for i in range(1,n+1):
        if visited[i]==m:
            if answer<i:
                answer=i
    print("#{} {}".format(test_case,answer))
