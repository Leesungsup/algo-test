def solution(N,numbers):
    answer=0
    dp=[[]]
    for i in range(1,9):
        temp=[]
        for j in range(1,i):
            for op1 in dp[i]:
                for op2 in dp[i-j]:
                    temp.append(op1+op2)
                    if op1-op2>0:
                        temp.append(op1-op2)
                    temp.append(op1*op2)
                    if op1!=0 and op2!=0:
                        temp.append(op1//op2)
        temp.append(int(str(N)*i))
        if numbers in temp:
            answer=i
            return answer
        dp.append(list(set(temp)))
    return -1