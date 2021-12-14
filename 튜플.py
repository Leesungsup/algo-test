import re
def solution(s):
    answer = []
    number=re.findall(r'\d+',s)
    d=dict()
    for i in number:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in range(len(d)):
        max=-987654321
        for j in d:
            if d[j]>max:
                max=d[j]
                k=j
        answer.append(int(k))
        d[k]=0
    print(answer)
    return answer
solution("{{20,111},{111}}")
