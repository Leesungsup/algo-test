def solution(genres,plays):
    answer=[]
    d=dict()
    num=-1
    for i in genres:
        if i not in d:
            num+=1
            d[i]=num
    graph=[[] for _ in range(len(d))]
    for i,g in enumerate(genres):
        if len(graph[d[g]])<2:
            graph[d[g]].append(i)
        else:
            if plays[graph[d[g]][0]]<plays[i]:
                graph[d[g]][0],graph[d[g]][1]=i,graph[d[g]][0]
            elif plays[graph[d[g]][1]]<play[i]:
                graph[d[g]][1]=i
    for i in d:
        graph[d[i]]=sorted(graph[d[i]],key=lambda x:plays[x],reverse=True)
    for i in sorted(graph,reverse=True):
        for j in i:
            answer.append(j)
    print(answer)
    return answer
genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
solution(genres,plays)