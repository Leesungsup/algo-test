def solution(participant, completion):
    d=dict()
    for i in participant:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in completion:
        d[i]-=1
    for i in d.keys():
        if d[i]!=0:
            answer=i
            break
    print(answer)

participant=list(map(str,input().split()))
completion=list(map(str,input().split()))
solution(participant,completion)
