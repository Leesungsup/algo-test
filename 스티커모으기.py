def solution(sticker):
    answer=0
    n=len(sticker)
    dp=[0]*n
    dp[0]=sticker[0]
    dp[1]=sticker[1]
    for i in range(2,n-1):
        dp[i]=max(dp[i-1],sticker[i]+dp[i-2])
    dp2=[0]*n
    dp2[0]=0
    dp2[1]=sticker[1]
    for i in range(2,n):
        dp2[i]=max(dp2[i-1],sticker[i]+dp2[i-2])
    return max(max(dp),max(dp2))