T=int(input())
for test_case in range(T):
    n,L=map(int,input().split())
    lst=[[0,0]]
    for i in range(n):
        lst.append(list(map(int,input().split())))
    dp=[[0]*(L+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,L+1):
            weight=lst[i][0]
            value=lst[i][1]
            if j>weight:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value)
    print("#{} {}".format(test_case,dp[n][L]))


T=int(input())
for test_case in range(1,T+1):
    n,L=map(int,input().split())
    lst=[[0,0]]
    dp=[[0]*(L+1) for _ in range(n)]
    for i in range(n):
        num,cal=map(int,input().split())
        lst.append([cal,num])
    for i in range(1,n+1):
        for j in range(1,L+1):
            weight=lst[i][0]
            value=lst[i][1]
            if j<weight:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value)
    print("#{} {}".format(test_case,dp[n][L]))