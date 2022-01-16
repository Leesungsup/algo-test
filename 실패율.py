from operator import itemgetter
def solution(N, stages):
    answer = []
    d=dict()
    sum=0
    for i in range(1,N+1):
        d[i]=stages.count(i)/(len(stages)-sum)
        sum+=stages.count(i)
    #print(d)
    sorted_dict = sorted(d, key = lambda x: d[x],reverse=True)
    #sorted_dict = sorted(d.items(), key = lambda x: x[1],reverse=True)
    #print([x[0] for x in sorted_dict])
    print(sorted_dict)
    #for i in sorted_dict:
    #answer.append(i[0])
    #print(answer)
    return sorted_dict
solution(5,[2, 1, 2, 6, 2, 4, 3, 3])
from operator import itemgetter
def solution(N, stages):
    answer = []
    d=dict()
    sum=0
    n=len(stages)
    for i in range(1,N+1):
        if n!=0:
            d[i]=stages.count(i)/(n)
            n-=stages.count(i)
        else:
            d[i]=0
    #print(d)
    sorted_dict = sorted(d, key = lambda x: d[x],reverse=True)
    #sorted_dict = sorted(d.items(), key = lambda x: x[1],reverse=True)
    #print([x[0] for x in sorted_dict])
    print(sorted_dict)
    #for i in sorted_dict:
    #answer.append(i[0])
    #print(answer)
    return sorted_dict
