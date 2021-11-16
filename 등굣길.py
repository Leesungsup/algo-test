from collections import deque
def solution(m,n,puddles):
    answer=0
    puddles = [[q,p] for [p,q] in puddles]
    map=[[0]*(m+1) for _ in range(n+1)]
    map[1][1]=1
    for i in range(1,(n+1)):
        for j in range(1,(m+1)):
            if i==1 and j==1:
                continue
            if [i,j] in puddles:
                map[i][j]=0
            else:
                map[i][j]=(map[i-1][j]+map[i][j-1]) % 1000000007
    answer=map[i][j]
    return answer
solution(4,3,[[2, 2]])
