def solution(matrix_sizes):
    answer=0
    n=len(matrix_sizes)
    dp=[[0]*n for _ in range(n)]
    for c in range(1,n):
        for i in range(0,n-c):
            j=i+c
            if c==1:
                dp[i][j]=matrix_sizes[i][0] * matrix_sizes[j][0] * matrix_sizes[j][1]
                continue
            dp[i][j]=float('inf')
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])
    return dp[0][n-1]