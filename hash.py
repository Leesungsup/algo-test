from collections import defaultdict
def solution4(genres,plays):
    answer=[]
    genre_dic=defaultdict(lambda :0)
    total_list=defaultdict(lambda:[])
    for i in range(len(genres)):
        genre_dic[genres[i]]+=plays[i]
        total_list[genres[i]].append((plays[i],i))
    genre_dic=sorted(genre_dic.items(),key=lambda x:x[1],reverse=True)
    for i in total_list:
        total_list[i]=sorted(total_list[i],key=lambda x:x[0],reverse=True)[:2]
    while len(genre_dic)>0:
        genre_max=genre_dic.pop(0)
        for t in total_list:
            if t==genre_max[0]:
                if len(total_list[t])>1:
                    answer.append(total_list[t][0][1])
                    answer.append(total_list[t][1][1])
                else:
                    answer.append(total_list[t][0][1])
    return answer
def solution3(clothes):
    answer=1
    d=dict()
    for i in clothes:
        if i[1] not in d:
            d[i[1]]=1
        if i[1] in d:
            d[i[1]]+=1
    for i in d:
        answer=answer*(d[i]+1)
    answer-=1
    return answer
def solution2(phone_book):
    answer=True
    phone_book.sort()
    for i in range(1,len(phone_book)):
        if phone_book[i].find(phone_book[i-1])==0:
            answer=False
            return answer
    return answer
def solution1(participant,completion):
    answer=''
    p=dict()
    for i in participant:
        if i not in p:
            p[i]=1
        if i in p:
            p[i]+=1
    for i in completion:
        if i in p:
            p[i]-=1
    for i in p:
        if p[i]!=0:
            answer=i
    print(p)
    return answer
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
    answer=1
    q=dict()
    for i in clothes:
        if i[1] not in q:
            q[i[1]]=1
        else:
            q[i[1]]+=1
    for i in q:
        answer=answer*(q[i]+1)
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