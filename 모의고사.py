
def solution1(answers):
    answer = []
    count=[0]*3
    j=[1,2,3,4,5]
    j1=[2,1,2,3,2,4,2,5]
    j2=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if j[i%5]==answers[i]:
            count[0]+=1
        if j1[i%8]==answers[i]:
            count[1]+=1
        if j2[i%10]==answers[i]:
            count[2]+=1
    m=-987654321
    index=0
    for i in range(3):
        if m<count[i]:
            m=count[i]
            index=i
    for i in range(3):
        if count[index]==count[i]:
            answer.append(i+1)
    return answer
def solution(answers):
    answer=[]
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
    print(answer)
answers=list(map(int,input().split()))
solution(answers)