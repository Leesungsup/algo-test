def solution(n,results):
    answer=0
    win={}
    lose={}
    for i in range(1,n+1):
        win[i]=set()
        lose[i]=set()
    for i in range(1,n+1):
        for j in results:
            if i==j[0]:
                win[i].add(j[1])
            if i==j[1]:
                lose[i].add(j[0])
        for j in win[i]:
            lose[j].update(lose[i])
        for j in lose[i]:
            win[j].update(win[i])
    for i in range(1,n+1):
        if len(win[i])+len(lose[i])==n-1:
            answer+=1
    print(answer)
    return answer
n=5
results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
solution(n,results)
def solution(n,results):
    answer=0
    graph=[[0]*(n+1) for _ in range(n+1)]
    for i in results:
        graph[i[0]][i[1]]=1
        graph[i[1]][i[0]]=-1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][j]==0:
                    if graph[i][k]==1 and graph[k][j]==1:
                        graph[i][j]=1
                    if graph[i][k]==-1 and graph[k][j]==-1:
                        graph[i][j]=-1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j]==0:
                answer+=1
    print(graph)
    return answer