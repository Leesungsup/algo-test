
def solution1(answers):
    answer = []
    count=[0]*3
    j=[-1]*3
    j2=[2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    j3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in answers:
        for k in range(3):
            j[k]+=1
        if j[0]>4:
            j[0]=0
        if j[1]>15:
            j[1]=0
        if j[2]>9:
            j[2]=0
        if j[0]+1==i:
            count[0]+=1
        if j2[j[1]]==i:
            count[1]+=1
        if j3[j[2]]==i:
            count[2]+=1
    ma=max(count)
    for i in range(3):
        if ma==count[i]:
            answer.append(i+1)
    return answer