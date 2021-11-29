def solution2(genres,plays):
    answer =[]
    genre_dic={}
    total_list={}
    for i in range(len(genres)):
        if genres[i] in genre_dic:
            genre_dic[genres[i]]+=plays[i]
            total_list[genres[i]].append((plays[i],i))
        else:
            genre_dic[genres[i]]=plays[i]
            total_list[genres[i]]=[(plays[i],i)]
    genre_dic=sorted(genre_dic.items(),key=lambda x:x[1],reverse=True)
    for i in total_list:
        total_list[i]=sorted(total_list,key=lambda x:x[0],reverse=True)[:2]
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
            elif plays[graph[d[g]][1]]<plays[i]:
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
def solution1(genres, plays):
    answer = []
    playDic = {}  # {장르 : 총 재생 횟수}
    dic = {}      # {장르 : [(플레이 횟수, 고유번호)]}

    # 해시 만들기
    for i in range(len(genres)):
        playDic[genres[i]] = playDic.get(genres[i], 0) + plays[i]
        dic[genres[i]] = dic.get(genres[i], []) + [(plays[i], i)]

    # 재생 횟수 내림차순으로 장르별 정렬
    genreSort = sorted(playDic.items(), key = lambda x: x[1], reverse = True)

    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, totalPlay) in genreSort:
        dic[genre] = sorted(dic[genre], key = lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in dic[genre][:2]]

    return answer