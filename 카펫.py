def solution(brown,yellow):
    answer=[]
    min=987654321
    for i in range(1,(brown+yellow)+1):
        for j in range(1,i+1):
            if i*j>(brown+yellow):
                break
            if i*j==(brown+yellow):
                if (i-2)*(j-2)==yellow:
                    if (i-j)>=0:
                        if i-j<min:
                            min=(i-j)
                            answer.append(i)
                            answer.append(j)
    print(answer)
brown,yellow=map(int,input().split())
solution(brown,yellow)
