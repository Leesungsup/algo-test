import copy
def solution(gems):
    answer = []
    d=dict()
    for i in gems:
        if i not in d:
            d[i]=1
    #print(d)
    d1=dict()
    d1=copy.deepcopy(d)
    #print(d1)
    n=len(d)
    #print(n)
    while True:
        for i in range(len(gems)):
            num=0
            if i+n<=len(gems):
                for j in range(i,i+n):
                    if d[gems[j]]==1:
                        d[gems[j]]=0
                for j in d:
                    if d[j]!=0:
                        num=1
                if num==0:
                    #print(i)
                    answer=[i+1,i+n]
                    break
                else:
                    d=copy.deepcopy(d1)
            else:
                num=1
        if num==0:
            break
        else:
            n+=1
    #print(answer)
    return answer
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
def solution(gems):
    answer = []
    shortest = len(gems)+1
    start_p = 0
    end_p = 0
    check_len = len(set(gems))
    contained = {}
    while end_p < len(gems):
        if gems[end_p] not in contained:
            contained[gems[end_p]] = 1
        else:
            contained[gems[end_p]] += 1
        end_p += 1
        if len(contained) == check_len:
            while start_p < end_p:
                if contained[gems[start_p]] > 1:
                    contained[gems[start_p]] -= 1
                    start_p += 1
                elif shortest > end_p - start_p:
                    shortest = end_p - start_p
                    answer = [start_p+1, end_p]
                    break
                else:
                    break
    return answer
