from collections import deque
def solution4(triangle):
    answer=0
    n=len(triangle)
    for i in range(1,n):
        for j in range(i+1):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif i==j:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
    ax=-987654321
    for i in range(n):
        if triangle[n-1][i]>ax:
            ax=triangle[n-1][i]
    answer=ax
    print(answer)
    return answer
def solution3(N,number):
    answer=0
    if N==number:
        return 1
    s=[set() for x in range(8)]
    for i,x in enumerate(s,start=1):
        x.add(int(str(N)*i))
    for i in range(1,8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2!=0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i + 1
            break
    if answer==0:
        answer=-1
        return answer
    return answer
def solution2(N, number):
    if N == number:
        return 1
    s = [ set() for x in range(8) ]
    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer
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
def solution1(triangle):
    answer=0
    n=len(triangle)
    for i in range(1,n):
        for j in range(1,i+1):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==i:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle+=max(triangle[i-1][j-1],triangle[i-1][j])