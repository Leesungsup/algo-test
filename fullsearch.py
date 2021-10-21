def solution(brown,yellow):
    answer=[]
    for i in range(1,(yellow+brown)//2+1):
        for j in range(1,i):
            if i*j>(yellow+brown):
                break
            if i*j==(yellow+brown):
                if (i-2)*(j-2)==yellow:
                    if i-j>=0:
                        if (i-j)<min:
                            min=(i-j)
                            answer.append(i)
                            answer.append(j)
    return answer