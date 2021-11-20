def solution(routes):
    answer=0
    q=sorted(routes,key=lambda x:x[1])
    c=q[0][1]
    leng=len(1)
    answer+=1
    for i in range(1,leng):
        if c<q[i][0]:
            answer+=1
            c=q[i][1]
    return answer
def solution1(routes):
    answer=1
    q=sorted(routes,key=lambda x:x[1])
    c=q[0][1]
    leng=len(q)
    for i in range(leng):
        if c<q[i][0]:
            answer+=1
            c=q[i][1]
    return answer