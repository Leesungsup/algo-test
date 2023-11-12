n=int(input())
arr=[int(input()) for _ in range(n)]
dp=[0]*n
dp1=[0]*n
if len(arr)<=2:
    print(sum(arr))
else:
    dp[0]=arr[0]
    dp[1]=arr[0]+arr[1]
    dp[2]=max(arr[0]+arr[2],arr[1]+arr[2],dp[1])
    for i in range(3,n):
        dp[i]=max(dp[i-3]+arr[i]+arr[i-1],dp[i-2]+arr[i])
        dp[i] = max(dp[i-1], dp[i])
    print(dp[-1])
    # print(dp)
    # dp1[0]=arr[0]
    # dp1[1]=arr[0]+arr[1]
    # dp1[2]=max(arr[0]+arr[2],arr[1]+arr[2])
    # for i in range(3,n-1):
    #     dp1[i]=max(dp1[i-3]+arr[i]+arr[i-1],dp1[i-2]+arr[i])
    # print(dp1[-1])
    # print(dp1)