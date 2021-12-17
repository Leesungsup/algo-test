from itertools import combinations
def solution(relation):
    answer = 0
    for k in range(len(relation[0])):
        q=[[] for _ in range(len(relation))]
        print(k)
        for i in range(len(relation[0])):
            d=dict()
            for j in range(len(relation)):
                q[j].append(relation[j][(i+k)%k])
                for g in combinations(q[j],i+1):
                    print(g)
                    if g not in d:
                        d[g]=1
                    else:
                        d[g]+=1
            print(d)
            if len(d.keys())==len(relation):
                answer+=1
                break

    """print(q)
    for i in range(len(relation[0])):
        print(len(q[i].keys()))
        if len(q[i].keys())==len(relation):
            answer+=1
            continue"""
    return answer
from collections import deque
def solution1(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates=[]
    for i in range(1,n_col+1):
        candidates.extend(combinations(range(n_col),i))
    print(candidates)
    final=[]
    for keys in candidates:
        tmp=[tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp))==n_row:
            final.append(keys)

    answer=set(final[:])
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i])==len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
import numpy as np
from itertools import combinations

def solution2(relation):
    answer = 0
    n_rel = np.array(relation).T # transpose(전치행렬). 더 편하게 column 접근가능
    candidates = [] # 정답 후보

    for grouping_num in range(1, len(n_rel)+1): # 유일성 확인. column 값, column의 인덱스 값 각각 combination
        comb = list(combinations([n_rel[i] for i in range(len(n_rel))], grouping_num))
        index_comb = list(combinations([i for i in range(len(n_rel))], grouping_num))
        for c in range(len(comb)):
            group = []
            for i in range(len(comb[c][0])): # 각 column의 인덱스 쌍을 만듬. [[100,ryan]...]
                group.append(tuple(comb[c][j][i] for j in range(len(comb[c]))))
            if len(group) == len(set(group)): # len([100,ryan]) == len(set([100,ryan])) ???
                candidates.append(set(index_comb[c]))

    for c in range(len(candidates[::-1])): # 최소성 확인
        check = True
        for i in range(c): # 어떤 하나라도 부분집합이 있으면, 정답 check false
            if candidates[i].issubset(candidates[c]):
                check = False
                break
        if check:
            answer += 1

    return answer
solution1([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
