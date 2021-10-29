from itertools import combinations
from collections import defaultdict
def solution(info,query):
    answer=[]
    dict=defaultdict(list)
    for i in info:
        g=i.split()
        i_key=g[:-1]
        i_value=int(g[-1])
        for j in range(5):
            for k in combinations(i_key,j):
                temp=''.join(k)
                dict[temp].append(i_value)
    for i in dict.keys():
        dict[i].sort()
    for i in query:
        q=i.split(' ')
        q_key=q[:-1]
        q_value=int(q[-1])
        while 'and' in q_key:
            q_key.remove('and')
        while '-' in q_key:
            q_key.remove('-')
        tmp_q=''.join(q_key)
        if tmp_q in dict:
            score=dict[q_key]
            if len(score)>0:
                left=0
                right=len(score)
                while left<right:
                    mid=(left+right)//2
                    if score[mid]>=q_value:
                        right=mid
                    else:
                        left=mid+1
                answer.append(len(score)-left)
        else:
            answer.append(0)
    return answer