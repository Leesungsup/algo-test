def solution1(m,n,puddles):
    answer=0
    puddles=[[q,p] for [p,q] in puddles]
    map = [[0]*(m+1) for _ in range(n+1)]
    map[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                break
            elif [i,j] in puddles:
                map[i][j]=0
            else:
                map[i][j]=(map[i-1][j]+map[i][j-1])%1000000007
    answer=map[i][j]
def solution(triangle):
    answer=0
    n=len(triangle)
    for i in range(1,n):
        for j in range(len(triangle[i])):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
    mx=-987654321
    for i in range(n):
        if triangle[n-1][i]>mx:
            mx=triangle[n-1][i]
    answer=mx
    print(answer)
    return answer
def solution(N,number):
    if N==number:
        return 1
    map=[set() for _ in range(8)]
    for i,x in enumerate(map, start=1):
        x.append(int(str(N)*i))
    for i in range(1,8):
        for j in range(i):
            for op1 in map[j]:
                for op2 in map[i-j-1]:
                    map[i].add(op1 + op2)
                    map[i].add(op1 - op2)
                    map[i].add(op1 * op2)
                    if op2 != 0:
                        map[i].add(op1 // op2)
        if number in map[i]:
            answer = i + 1
            break
        else:
            answer = -1
    return answer
def solution(money):
    dp=[0]*len(money)
    dp[0]=money[0]
    dp[1]=max(money[0],money[1])
    for i in range(2,len(money)):
        dp[i]=max(dp[i-1],dp[i-2]+money[i])
    dp1=[0]*len(money)
    dp1[0]=0
    dp1[1]=money[1]
    for i in range(2,len(money)):
        dp1[i]=max(dp1[i-1],dp[i-2]+money[i])
    return max(max(dp),max(dp1))
def solution(coins, change):
    dp = [999999] * (change + 1)
    dp[0] = 0
    for i in range(len(coins)):
        for j in range(1, change):
            dp[j] = min(dp[j], dp[j - coins[i]])

    return dp[change]