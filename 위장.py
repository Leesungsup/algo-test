def solution(clothes):
    answer=1
    d=dict()
    for i in clothes:
        if i[1] not in d:
            d[i[1]]=1
        else:
            d[i[1]]+=1
    for i in d:
        answer=answer*(d[i]+1)
    answer-=1
    print(answer)
    return answer
clothes=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)