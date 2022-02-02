def solution(n):
    answer=[]
    numArr = [[0]*i for i in range(1,n+1)]
    row=-1
    col=0
    print(numArr)
    curNum = 1
    for i in range(n,0,-3):
        print(i)
        for j in range(i) :
            row+=1
            numArr[row][col] = curNum
            curNum+=1
        for j in range(i-1) :
            col+=1
            numArr[row][col] = curNum
            curNum+=1
        for j in range(i-2) :
            row-=1
            col-=1
            numArr[row][col] = curNum
            curNum+=1
    for i in numArr:
        for j in i:
            answer.append(j)
    return answer
print(solution(4))
