from collections import defaultdict
def solution(participant,completion):
    answer=''
    p=dict()
    for i in participant:
        if i not in p:
            p[i]=1
        else:
            p[i]+=1
    for i in completion:
        if i in p:
            p[i]-=1
    for i in p:
        if p[i]!=0:
            answer=i
    return answer
def solution1(phone_book):
    answer=True
    phone_book.sort()
    for i in range(len(phone_book)):
        if phone_book[i].find(phone_book[i-1])==0:
            answer=False
            return answer
    return answer
def solution2(clothes):
    answer=0
    q=dict()
    for i in clothes:
        if i[1] not in q:
            q[i[1]]=1
        else:
            q[i[1]]+=1
    for i in q:
        answer=answer*(d[i]+1)
    answer-=1
    print(answer)
    return answer
def solution3(genres, plays):
    answer = []
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
            elif plays[graph[d[g]][1]]<plays[i]:
                graph[d[g]][1]=i
    for i in d:
        graph[d[i]]=sorted(graph[d[i]],key=lambda x:plays[x],reverse=True)
    for i in sorted(graph,reverse=True):
        for j in i:
            answer.append(j)
    return answer